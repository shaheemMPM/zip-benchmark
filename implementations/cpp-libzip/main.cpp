#include <iostream>
#include <fstream>
#include <vector>
#include <zip.h>
#include <filesystem>
#include <chrono>

namespace fs = std::filesystem;

void zipPdfs(const fs::path& inputDir, const fs::path& outputDir) {
    std::cout << "Started zip generation with cpp-libzip" << std::endl;

    auto now = std::chrono::system_clock::now();
    auto timestamp = std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch()).count();
    fs::path zipFilename = outputDir / fs::path("cpp-libzip-" + std::to_string(timestamp) + ".zip");

    int err = 0;
    zip_t* zip = zip_open(zipFilename.c_str(), ZIP_CREATE | ZIP_TRUNCATE, &err);
    if (!zip) {
        std::cerr << "Failed to create zip file: " << zipFilename << std::endl;
        return;
    }

    for (const auto& entry : fs::recursive_directory_iterator(inputDir)) {
        if (entry.is_regular_file() && entry.path().extension() == ".pdf") {
            std::ifstream file(entry.path(), std::ios::binary);
            if (!file) {
                std::cerr << "Failed to open file: " << entry.path() << std::endl;
                continue;
            }

            std::vector<char> buffer(std::istreambuf_iterator<char>(file), {});
            fs::path relativePath = fs::relative(entry.path(), inputDir);
            zip_source_t* source = zip_source_buffer(zip, buffer.data(), buffer.size(), 0);
            if (zip_file_add(zip, relativePath.c_str(), source, ZIP_FL_ENC_UTF_8) < 0) {
                zip_source_free(source);
                std::cerr << "Failed to add file to zip: " << entry.path() << std::endl;
            }
        }
    }

    zip_close(zip);
    std::cout << "Zip file created: " << zipFilename << std::endl;
}

int main() {
    fs::path inputDir = "../../common/test_data/sample_pdfs";
    fs::path outputDir = "../../output";

    if (!fs::exists(outputDir)) {
        fs::create_directories(outputDir);
    }

    zipPdfs(inputDir, outputDir);
    return 0;
}
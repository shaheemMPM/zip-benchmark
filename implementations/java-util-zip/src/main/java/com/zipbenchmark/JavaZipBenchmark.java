package com.zipbenchmark;

import java.io.*;
import java.nio.file.*;
import java.util.zip.*;
import java.time.Instant;

public class JavaZipBenchmark {
    public static void zipPdfs(Path inputDir, Path outputDir) throws IOException {
        if (!Files.exists(outputDir)) {
            Files.createDirectories(outputDir);
        }

        String timestamp = String.valueOf(Instant.now().getEpochSecond());
        Path zipFilename = outputDir.resolve("java-util-zip-" + timestamp + ".zip");

        try (ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(zipFilename.toFile()))) {
            Files.walk(inputDir)
                .filter(path -> !Files.isDirectory(path))
                .filter(path -> path.toString().toLowerCase().endsWith(".pdf"))
                .forEach(path -> {
                    ZipEntry zipEntry = new ZipEntry(inputDir.relativize(path).toString());
                    try {
                        zos.putNextEntry(zipEntry);
                        Files.copy(path, zos);
                        zos.closeEntry();
                    } catch (IOException e) {
                        System.err.println("Failed to add file to zip: " + path);
                        e.printStackTrace();
                    }
                });
        }

        System.out.println("Zip file created: " + zipFilename);
    }

    public static void main(String[] args) {
        try {
            Path inputDir = Paths.get("../../common/test_data/sample_pdfs");
            Path outputDir = Paths.get("../../output");
            zipPdfs(inputDir, outputDir);
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
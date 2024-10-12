use chrono::Local;
use std::fs::File;
use std::io::{Read, Write};
use std::path::{Path, PathBuf};
use zip::write::FileOptions;
use zip::CompressionMethod;
use zip::ZipWriter;

fn zip_pdfs(input_dir: &Path, output_dir: &Path) -> std::io::Result<PathBuf> {
    std::fs::create_dir_all(output_dir)?;

    let timestamp = Local::now().format("%Y%m%d_%H%M%S").to_string();
    let zip_filename = output_dir.join(format!("rust-zip-rs-{}.zip", timestamp));

    let file = File::create(&zip_filename)?;
    let mut zip = ZipWriter::new(file);

    let options: FileOptions<'_, ()> = FileOptions::default()
        .compression_method(CompressionMethod::Deflated)
        .unix_permissions(0o755);

    let mut buffer = Vec::new();
    for entry in std::fs::read_dir(input_dir)? {
        let entry = entry?;
        let path = entry.path();
        if path.is_file() && path.extension().map_or(false, |ext| ext == "pdf") {
            let name = path.strip_prefix(input_dir).unwrap().to_str().unwrap();
            zip.start_file(name, options)?;
            let mut f = File::open(path)?;
            f.read_to_end(&mut buffer)?;
            zip.write_all(&buffer)?;
            buffer.clear();
        }
    }

    zip.finish()?;
    println!("Zip file created: {:?}", zip_filename);
    Ok(zip_filename)
}

fn main() -> std::io::Result<()> {
    let input_dir = PathBuf::from("../../common/test_data/sample_pdfs");
    let output_dir = PathBuf::from("../../output");

    zip_pdfs(&input_dir, &output_dir)?;
    Ok(())
}

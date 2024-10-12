import os
import zipfile
from datetime import datetime


def zip_pdfs(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = os.path.join(output_dir, f"python-zipfile-{timestamp}.zip")

    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.lower().endswith(".pdf"):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, input_dir)
                    zipf.write(file_path, arcname)

    print(f"Zip file created: {zip_filename}")
    return zip_filename


if __name__ == "__main__":
    input_dir = os.path.join("..", "..", "common", "test_data", "sample_pdfs")
    output_dir = os.path.join("..", "..", "output")
    zip_pdfs(input_dir, output_dir)

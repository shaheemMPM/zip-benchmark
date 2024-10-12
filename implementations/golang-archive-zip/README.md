# Go archive/zip Implementation

This implementation uses Go's built-in `archive/zip` package to compress PDF files.

## Prerequisites

Ensure you have Go (v1.16+) installed on your system.

## Setup

1. Navigate to this directory:
   ```bash
   cd implementations/golang-archive-zip
   ```
2. The Go module is already initialized. If you need to add any dependencies (which is not necessary for this implementation), you can use `go get`.

## Running the benchmark

From the project root, run:

```bash
./implementations/golang-archive-zip/benchmark
```

This will compile and run the Go script to compress the PDF files.

## Implementation Details

- The main script is located in `src/main.go`.
- It uses the standard library's `archive/zip` package to create zip files.
- The script reads PDF files from the common test data directory and compresses them into a single zip file.
- The implementation walks through the input directory, adding each PDF file to the zip archive.

## Customization

You can modify `src/main.go` to adjust compression levels or other zip options if needed.

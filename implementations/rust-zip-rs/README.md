# Rust zip-rs Implementation

This implementation uses the `zip` crate in Rust to compress PDF files.

## Prerequisites

Ensure you have Rust and Cargo installed on your system. If not, you can install them from [https://www.rust-lang.org/](https://www.rust-lang.org/).

## Setup

1. Navigate to this directory:
   ```bash
   cd implementations/rust-zip-rs
   ```
2. Build the release version
   ```bash
   cargo build --release
   ```
3. The Rust project is already initialized with the necessary dependencies. If you need to update or add any dependencies, you can modify the `Cargo.toml` file and run `cargo build`.

## Running the benchmark

From the project root, run:

```bash
./implementations/rust-zip-rs/benchmark
```

This will compile the Rust program in release mode and run it to compress the PDF files.

## Implementation Details

- The main script is located in `src/main.rs`.
- It uses the `zip` crate to create zip files.
- The script reads PDF files from the common test data directory and compresses them into a single zip file.
- The implementation walks through the input directory, adding each PDF file to the zip archive.

## Customization

You can modify `src/main.rs` to adjust compression levels or other zip options if needed. The `zip` crate provides various options for customization.

# C++ libzip Implementation

This implementation uses C++ with the libzip library to compress PDF files.

## Prerequisites

- C++ compiler with C++17 support
- CMake (version 3.10 or later)
- libzip library

## Setup

1. Ensure you have libzip installed. If not, follow the instructions in the main setup guide.
2. Navigate to this directory:
   ```bash
   cd implementations/cpp-libzip
   ```
3. Build the project
   ```bash
    sh build.sh
   ```

## Running the benchmark

From the project root, run:

```bash
./implementations/cpp-libzip/benchmark
```

This will run the pre-built binary to compress the PDF files.

## Implementation Details

- The main script is located in `main.cpp`.
- It uses the `libzip` library to create zip files.
- The implementation walks through the input directory, adding each PDF file to the zip archive.
- CMake is used for building the project.

## Customization

You can modify `main.cpp` to adjust compression levels or other zip options if needed.

# Setup Guide

This guide will help you set up the Zip Benchmarking Project on your local machine.

## Prerequisites

Ensure you have the following installed:

- Git
- Node.js (v14+)
- Go (v1.16+)
- Rust (latest stable)
- Python (v3.8+)
- C++ compiler (g++ or clang++)
- Java Development Kit (JDK 11+)
- 7-Zip
- libzip
- GNU Time

### Installing 7-Zip

7-Zip is required for the Node.js 7-Zip implementation. Here's how to install it on different operating systems:

- On macOS:

  ```
  brew install p7zip
  ```

- On Ubuntu/Debian:

  ```
  sudo apt-get install p7zip-full
  ```

- On Windows:
  Download and install from the [7-Zip website](https://www.7-zip.org/)

After installing 7-Zip, ensure it's accessible from the command line by running:

```
7z --help
```

If you see the 7-Zip help message, the installation was successful.

### Installing libzip

libzip is required for the C++ implementation. Here's how to install it on different operating systems:

- On macOS:

  ```
  brew install libzip
  ```

- On Ubuntu/Debian:

  ```
  sudo apt-get install libzip-dev
  ```

- On Windows:
  Download and install from the [libzip website](https://libzip.org/download/)

After installing libzip, ensure it's accessible from the command line by running:

```
pkg-config --modversion libzip
```

If you see a version number, the installation was successful.

### Installing GNU Time

GNU Time is required for accurate benchmarking. Here's how to install it on different operating systems:

- On macOS:

  ```bash
  brew install gnu-time
  ```

  After installation, you can use it with the command gtime.

- On Ubuntu/Debian: GNU Time is usually pre-installed. If not, you can install it with:

  ```bash
  sudo apt-get install time
  ```

  You can use it with the command time.

- On Windows: GNU Time is not natively available. Consider using Windows Subsystem for Linux (WSL) and follow the Ubuntu/Debian instructions.

After installing GNU Time, ensure it's accessible from the command line:

- On macOS: `gtime --version`
- On Linux: `time --version`

If you see version information, the installation was successful.

## Installation Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/shaheemMPM/zip-benchmark.git
   cd zip-benchmark
   ```

2. Set up each implementation:

- Node.js (jszip and 7zip):

  ```sh
  cd implementations/nodejs-jszip && yarn install
  cd ../nodejs-7zip && yarn install
  ```

- Go:

  ```sh
  cd implementations/golang-archive-zip && go mod tidy
  go build -o release -ldflags="-s -w" -trimpath
  ```

- Rust:

  ```sh
  cd implementations/rust-zip-rs && cargo build --release
  ```

- Python:

  ```sh
  cd implementations/python-zipfile && pip install -r requirements.txt
  ```

- C++:

  ```sh
  cd implementations/cpp-libzip && sh build.sh
  ```

- Java:

  ```sh
  cd implementations/java-util-zip && mvn install
  ```

3. Generate test data:

   ```sh
   python common/utils/file_generator.py
   ```

You're now ready to run benchmarks!

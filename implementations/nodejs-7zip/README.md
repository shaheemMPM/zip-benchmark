# Node.js 7-Zip Implementation

This implementation uses Node.js with the `node-7z` library to compress PDF files using 7-Zip.

## Prerequisites

- Ensure you have Node.js (v14+) installed.
- 7-Zip must be installed on your system and accessible from the command line.

## Setup

1. Install 7-Zip if not already installed:

   - On macOS: `brew install p7zip`
   - On Ubuntu/Debian: `sudo apt-get install p7zip-full`
   - On Windows: Download and install from the [7-Zip website](https://www.7-zip.org/)

2. Install Node.js dependencies:
   ```
   yarn install
   ```

## Running the benchmark

From the project root, run:

```
./implementations/nodejs-7zip/benchmark
```

This will execute the Node.js script using 7-Zip to compress the PDF files.

## Implementation Details

- The main script is located in `src/index.js`.
- It uses the `node-7z` library, which is a Node.js wrapper for 7-Zip.
- The script reads PDF files from the common test data directory and compresses them into a single 7z file.
- A progress bar is displayed to show the compression progress.

## Customization

You can modify `src/index.js` to adjust compression levels or other 7-Zip options if needed.

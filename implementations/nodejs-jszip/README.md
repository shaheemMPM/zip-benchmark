# Node.js JSZip Implementation

This implementation uses Node.js with the JSZip library to compress PDF files.

## Setup

1. Ensure you have Node.js (v14+) installed.
2. Install dependencies:
   ```
   yarn install
   ```

## Running the benchmark

From the project root, run:

```
./implementations/nodejs-jszip/benchmark
```

This will execute the Node.js script using JSZip to compress the PDF files.

## Implementation Details

- The main script is located in `src/index.js`.
- It uses the `jszip` library to create zip files.
- The script reads PDF files from the common test data directory and compresses them into a single zip file.
- A progress bar is displayed to show the compression progress.

## Customization

You can modify `src/index.js` to adjust compression levels or other JSZip options if needed.

# Zip Benchmarking Project

This project aims to benchmark the performance of various programming language and library combinations for zipping large numbers of PDF files efficiently.

## Implementations

- Node.js with jszip
- Node.js with 7zip
- Go with archive/zip
- Rust with zip-rs
- Python with zipfile
- C++ with libzip
- Java with java.util.zip

> Note: All current implementations are single-threaded and use default compression settings.

## Getting Started

1. Clone this repository
2. Follow the setup instructions in [`docs/setup.md`](./docs/setup.md)
3. Run benchmarks using the instructions in [`docs/running_benchmarks.md`](./docs/running_benchmarks.md)
4. Analyze results using the guide in [`docs/analyzing_results.md`](./docs/analyzing_results.md)

## Project Structure

- `implementations/`: Contains individual implementations for each language-library combo
- `benchmark/`: Scripts for running benchmarks and storing results
- `common/`: Shared resources and utilities
- `docs/`: Project documentation

## Benchmark Results

Latest benchmark performed on MacBook Air M2 (16GB RAM, macOS Sonoma 14.6.1) with 30,000 PDFs (total size: 8.56 GB), single-threaded operations using default compression settings:

> **Detailed Results**: View the complete benchmark results with interactive sorting at [https://shaheemmpm.github.io/zip-benchmark/](https://shaheemmpm.github.io/zip-benchmark/)

### Key Findings

1. **Execution Time**:

   - Node.js implementations (7zip and jszip) are the fastest, completing in under 1 minute
   - Go, Rust, Python, and Java implementations perform similarly, taking 2-3 minutes
   - C++ implementation with libzip is notably slower, taking over 43 minutes

2. **Memory Usage**:

   - Most implementations are memory efficient (23-34 MB)
   - Java implementation uses moderate memory (233 MB)
   - Node.js jszip implementation has high memory usage (8.6 GB), suggesting potential memory management issues

3. **Compression Ratio**:
   - C++ libzip achieves the best compression ratio at 54.92%
   - Most other implementations achieve consistent compression ratios around 17%
   - Node.js jszip shows negligible compression (-0.05%)

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

### Potential Improvements

- Implement multi-threading support for better performance
- Experiment with different compression levels and algorithms
- Optimize memory usage, particularly for Node.js jszip implementation
- Add progress tracking and pause/resume capabilities
- Implement chunking for handling larger datasets

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

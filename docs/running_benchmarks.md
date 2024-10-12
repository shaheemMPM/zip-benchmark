# Running Benchmarks

This guide explains how to run benchmarks for the Zip Benchmarking Project.

## Preparation

1. Ensure you've completed all steps in the setup guide (`docs/setup.md`).
2. Make sure you have sufficient disk space for benchmark results.

## Running All Benchmarks

To run benchmarks for all implementations:

1. Navigate to the project root.
2. Run the benchmark script:

   ```sh
   ./benchmark/scripts/run
   ```

   This script will:

   - Run each implementation with various file sizes and quantities.
   - Store results in `benchmark/results/`.

## Running Individual Benchmarks

To benchmark a specific implementation:

1. Navigate to the implementation directory.
2. Run the implementation-specific benchmark script. For example:
   ```sh
   cd implementations/rust-zip-rs
   ./benchmark
   ```

## Customizing Benchmarks

You can customize benchmark parameters by editing `benchmark/scripts/run` or the individual implementation benchmark scripts.

Key parameters to consider:

- Number of files
- File sizes
- Compression levels

Remember to document any changes you make to ensure consistent comparisons.

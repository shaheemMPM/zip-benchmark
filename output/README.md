# Output Directory

This directory is used to store the zip files generated by the various implementations in the Zip Benchmarking Project.

## Purpose

The `output` directory serves as a centralized location for all zip files produced during the benchmarking process. This allows for easy comparison and analysis of the results from different implementations.

## Usage

- Each implementation should save its generated zip files to this directory.
- The naming convention for output files should be:
  `{implementation}-{timestamp}.zip`
  For example: `nodejs-jszip-20230515120000.zip`

## Management

- This directory is included in the repository structure, but its contents (except for this README) are ignored by git to avoid committing large binary files.
- After running benchmarks and analyzing results, you may want to clean this directory to free up disk space.
- Consider keeping only the most recent or relevant zip files for ongoing analysis.

## Notes

- Ensure you have sufficient disk space available, especially when running benchmarks with large datasets.
- If you're sharing benchmark results, consider using file sharing services for the zip files rather than committing them to the repository.

## Cleaning Up

You can use the following command to remove all zip files from this directory:

```bash
find . -maxdepth 1 -name "*.zip" -type f -delete
```

Remember to run this command from within the `output` directory.

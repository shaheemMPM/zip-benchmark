# Java util.zip Implementation

This implementation uses Java's built-in `java.util.zip` package to compress PDF files.

## Prerequisites

- Java Development Kit (JDK) 11 or later
- Apache Maven

## Setup

1. Ensure you have JDK and Maven installed. If not, follow the instructions in the main setup guide.
2. Navigate to this directory:
   ```bash
   cd implementations/java-util-zip
   ```
3. Build the project:

   ```bash
   mvn clean package
   ```

## Running the benchmark

From the project root, run:

```bash
./implementations/java-util-zip/benchmark
```

This will run the Java program to compress the PDF files.

## Implementation Details

- The main class is `JavaZipBenchmark` in the `com.zipbenchmark` package.
- It uses the `java.util.zip` package to create zip files.
- The implementation walks through the input directory, adding each PDF file to the zip archive.
- Maven is used for building and managing the project.

## Customization

You can modify `JavaZipBenchmark.java` to adjust compression levels or other zip options if needed.

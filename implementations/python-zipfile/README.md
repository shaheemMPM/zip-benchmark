# Python zipfile Implementation

This implementation uses Python's built-in `zipfile` module to compress PDF files.

## Setup

1. Ensure you have Python 3.8+ installed.
2. Set up the virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the benchmark

From the project root, run:

```
./implementations/python-zipfile/benchmark
```

This will activate the virtual environment, run the Python script, and deactivate the virtual environment.

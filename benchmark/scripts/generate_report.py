import os
import sys
from datetime import datetime


def parse_result_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    execution_time = "N/A"
    memory_usage = "N/A"
    compression_ratio = "N/A"

    for line in content.split("\n"):
        if "real" in line:
            execution_time = line.split()[1]
        elif "maximum resident set size" in line.lower():
            memory_usage = line.split()[-1] + " KB"
        elif "compression ratio:" in line.lower():
            compression_ratio = line.split(":")[1].strip()

    return {
        "execution_time": execution_time,
        "memory_usage": memory_usage,
        "compression_ratio": compression_ratio,
    }


def generate_report(results_dir):
    report = "# Zip Benchmark Report\n\n"
    report += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    report += "| Implementation | Execution Time | Memory Usage | Compression Ratio |\n"
    report += "|----------------|----------------|--------------|-------------------|\n"

    for file in os.listdir(results_dir):
        if file.endswith("_result.txt"):
            impl_name = file.replace("_result.txt", "")
            result = parse_result_file(os.path.join(results_dir, file))
            report += f"| {impl_name} | {result['execution_time']} | {result['memory_usage']} | {result['compression_ratio']} |\n"

    report += "\n## Conclusions\n\n"
    report += "Add your analysis and conclusions here.\n"

    report_file = os.path.join(results_dir, "report.md")
    with open(report_file, "w") as f:
        f.write(report)

    print(f"Report generated: {report_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_report.py <results_directory>")
        sys.exit(1)

    results_dir = sys.argv[1]
    generate_report(results_dir)

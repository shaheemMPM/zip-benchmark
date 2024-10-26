import os
import sys
from datetime import datetime

from jinja2 import Environment, FileSystemLoader


def parse_result_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    execution_time = "N/A"
    memory_usage = "N/A"
    compression_ratio = "N/A"

    for line in content.split("\n"):
        if "Elapsed (wall clock) time" in line:
            # Extract the time part (e.g., "43:09.98" or "2:04.68")
            time_str = (
                line.split(":")[-2:][0].strip() + ":" + line.split(":")[-1].strip()
            )

            # Split into minutes and seconds.milliseconds
            if time_str.count(":") == 2:  # Format is h:mm:ss.ms
                _, minutes, seconds = time_str.split(":")
            else:  # Format is m:ss.ms
                minutes, seconds = time_str.split(":")

            # Convert to total seconds
            total_seconds = int(minutes) * 60 + float(seconds)
            execution_time = f"{total_seconds:.2f}"

        elif "Maximum resident set size (kbytes)" in line:
            memory_kb = int(line.split(":")[-1].strip())
            memory_usage = f"{memory_kb // 1024} MB"
        elif "Compression Ratio:" in line:
            compression_ratio = line.split(":")[-1].strip()

    return {
        "execution_time": execution_time,
        "memory_usage": memory_usage,
        "compression_ratio": compression_ratio,
    }


def generate_report(results_dir):
    results = []
    for file in os.listdir(results_dir):
        if file.endswith("_result.txt"):
            impl_name = file.replace("_result.txt", "")
            result = parse_result_file(os.path.join(results_dir, file))
            results.append(
                {
                    "implementation": impl_name,
                    "execution_time": result["execution_time"],
                    "memory_usage": result["memory_usage"],
                    "compression_ratio": result["compression_ratio"],
                }
            )

    template_dir = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("report_template.html")

    html_content = template.render(
        generated_on=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), results=results
    )

    report_file = os.path.join(results_dir, "report.html")
    with open(report_file, "w") as f:
        f.write(html_content)

    print(f"Report generated: {report_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_report.py <results_directory>")
        sys.exit(1)

    results_dir = sys.argv[1]
    generate_report(results_dir)

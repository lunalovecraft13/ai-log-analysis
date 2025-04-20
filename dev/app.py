# dev/app.py

import os
import sys
import platform
import matplotlib.pyplot as plt

# 🔌 Analyze logs for anomalies and count severity levels
# Returns: 
#   - List of anomalies (WARNING or ERROR)
#   - Dictionary with severity counts
def analyze_logs(logs):
    anomalies = []
    severity_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in logs:
        line = line.strip()
        if "ERROR" in line:
            anomalies.append(line)
            severity_counts["ERROR"] += 1
        elif "WARNING" in line:
            anomalies.append(line)
            severity_counts["WARNING"] += 1
        elif "INFO" in line:
            severity_counts["INFO"] += 1

    return anomalies, severity_counts

# 📋 Print each log line with line numbers and annotation symbols (🚨 for warnings/errors)
# Optionally filter by severity if a filter_level is passed (e.g., only show ERROR lines)
def display_logs_with_annotations(logs, filter_level=None):
    print("\n📘 Log File Contents (with annotations):\n")
    for i, line in enumerate(logs, start=1):
        line = line.strip()

        # Skip if filtering and this line doesn't match the severity level
        if filter_level and filter_level not in line:
            continue

        # Highlight anomaly logs
        if "ERROR" in line or "WARNING" in line:
            print(f"{i:03d}: 🚨 {line}")
        else:
            print(f"{i:03d}:     {line}")

# 🌈 Generate and save a bar chart visualizing log severity counts
# Output: 'log_severity_summary.png'
def plot_severity_counts(severity_counts):
    labels = list(severity_counts.keys())
    counts = list(severity_counts.values())

    plt.figure(figsize=(6, 4))
    plt.bar(labels, counts, color='orange')
    plt.title("Log Severity Levels")
    plt.xlabel("Severity")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("log_severity_summary.png")  # 📂 Save chart to file
    plt.show()  # Display in a pop-up window

# 🥧 Generate and save a pie chart showing percentage of each severity
# Output: 'log_severity_pie_chart.png'
def plot_pie_chart(severity_counts):
    labels = severity_counts.keys()
    sizes = severity_counts.values()
    colors = ['#66b3ff', '#ffcc99', '#ff6666']  # Custom colors for each level

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Log Severity Distribution')
    plt.axis('equal')  # Ensures pie is a circle
    plt.savefig("log_severity_pie_chart.png")  # 📂 Save pie chart to file
    print("🖼️ Pie chart saved as log_severity_pie_chart.png")
    plt.show()

# ⚙️ Main script entry point
# Handles file reading, filtering, anomaly detection, and visualization
def main():
    print("\n🚀 Test environment deployment started...")
    print(f"⚒️ Python Version: {platform.python_version()}")

    # Optional CLI severity filter passed as first argument (e.g., ERROR, INFO)
    filter_level = None
    if len(sys.argv) > 1:
        filter_level = sys.argv[1].upper()
        print(f"\n🔍 Filtering log output by severity: {filter_level}")

    # Path to the log file (adjust as needed)
    log_file = "logs/sample_logs.txt"
    print(f"\n📄 Reading logs from: {log_file}")

    # Exit early if file does not exist
    if not os.path.exists(log_file):
        print(f"❌ Log file not found: {log_file}")
        return

    # Read all lines from the file
    with open(log_file, "r") as file:
        logs = file.readlines()

    # Show logs line-by-line with annotations and optional filtering
    display_logs_with_annotations(logs, filter_level)

    # Analyze logs for errors, warnings, and info counts
    anomalies, severity_counts = analyze_logs(logs)

    # Print out a quick summary of severity counts
    print("\n🔹 Summary:")
    for level, count in severity_counts.items():
        print(f"- {level}: {count} entries")

    # Print all detected anomalies
    if anomalies:
        print("\n🚨 Anomalies Detected:")
        for entry in anomalies:
            print(f"  - {entry}")
    else:
        print("\n✅ No anomalies detected.")

    print("\n📊 Log analysis complete. Test stage deployment successful.")

    # Generate visual summaries
    plot_severity_counts(severity_counts)
    plot_pie_chart(severity_counts)

# 🔁 If this file is being run directly (not imported), start the app
if __name__ == "__main__":
    main()

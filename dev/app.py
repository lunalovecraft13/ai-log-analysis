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

# 📋 Display log lines with line numbers and annotation symbols (🚨 for anomalies)
# Optionally filter logs by severity level (e.g., only show ERROR entries)
def display_logs_with_annotations(logs, filter_level=None):
    print("\n📘 Log File Contents (with annotations):\n")
    for i, line in enumerate(logs, start=1):
        line = line.strip()

        # If a filter is set and this line doesn't match it, skip
        if filter_level and filter_level not in line:
            continue

        if "ERROR" in line or "WARNING" in line:
            print(f"{i:03d}: 🚨 {line}")
        else:
            print(f"{i:03d}:     {line}")

# 🌈 Generate and save a bar chart showing number of INFO, WARNING, and ERROR logs
def plot_severity_counts(severity_counts):
    labels = list(severity_counts.keys())
    counts = list(severity_counts.values())

    plt.figure(figsize=(6, 4))
    plt.bar(labels, counts, color='orange')
    plt.title("Log Severity Levels")
    plt.xlabel("Severity")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("log_severity_summary.png")
    plt.show()

# 🥧 Generate and save a pie chart showing the percentage of each log severity
def plot_pie_chart(severity_counts):
    labels = severity_counts.keys()
    sizes = severity_counts.values()
    colors = ['#66b3ff', '#ffcc99', '#ff6666']  # INFO, WARNING, ERROR colors

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title("Log Severity Distribution")
    plt.axis("equal")
    plt.savefig("log_severity_pie_chart.png")
    print("🖼️ Pie chart saved as log_severity_pie_chart.png")
    plt.show()

# 📝 Export all detected anomalies to a text file for audit or debugging
def export_anomalies(anomalies, filename="anomalies_report.txt"):
    with open(filename, "w") as f:
        for entry in anomalies:
            f.write(entry + "\n")
    print(f"\n📝 Anomalies written to {filename}")

# ⚙️ Main script that orchestrates the log reading, analysis, and reporting
def main():
    print("\n🚀 Test environment deployment started...")
    print(f"⚒️ Python Version: {platform.python_version()}")

    # Allow optional filtering by severity from command line argument
    filter_level = None
    if len(sys.argv) > 1:
        filter_level = sys.argv[1].upper()
        print(f"\n🔍 Filtering log output by severity: {filter_level}")

    # Path to sample log file (can be replaced with any log source)
    log_file = "logs/sample_logs.txt"
    print(f"\n📄 Reading logs from: {log_file}")

    # Exit if file is missing
    if not os.path.exists(log_file):
        print(f"❌ Log file not found: {log_file}")
        return

    # Read logs into a list
    with open(log_file, "r") as file:
        logs = file.readlines()

    # Display logs to terminal with annotations and filtering
    display_logs_with_annotations(logs, filter_level)

    # Analyze the logs for anomalies and severity counts
    anomalies, severity_counts = analyze_logs(logs)

    # Display severity summary
    print("\n🔹 Summary:")
    for level, count in severity_counts.items():
        print(f"- {level}: {count} entries")

    # Output anomaly results
    if anomalies:
        print("\n🚨 Anomalies Detected:")
        for entry in anomalies:
            print(f"  - {entry}")
        export_anomalies(anomalies)
    else:
        print("\n✅ No anomalies detected.")

    print("\n📊 Log analysis complete. Test stage deployment successful.")

    # Save visual charts to file
    plot_severity_counts(severity_counts)
    plot_pie_chart(severity_counts)

# 🔁 Run main if script is executed directly
if __name__ == "__main__":
    main()

# dev/app.py

import os
import sys
import platform
import matplotlib.pyplot as plt

# 📊 Analyze logs and count severity levels
# Returns a tuple of (anomalies list, severity_counts dictionary)
def analyze_logs(logs):
    anomalies = []
    severity_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

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

# 📄 Display logs with line numbers and highlight anomalies
# Optionally filters based on severity level
def display_logs_with_annotations(logs, filter_level=None):
    print("\n📘 Log File Contents (with annotations):\n")
    for i, line in enumerate(logs, start=1):
        line = line.strip()
        if filter_level and filter_level not in line:
            continue
        if "ERROR" in line or "WARNING" in line:
            print(f"{i:03d}: 🚨 {line}")
        else:
            print(f"{i:03d}:     {line}")

# 📊 Generate and save a bar chart showing severity counts
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

# 🥧 Generate and save a pie chart for severity distribution
def plot_pie_chart(severity_counts):
    labels = severity_counts.keys()
    sizes = severity_counts.values()
    colors = ['#66b3ff', '#ffcc99', '#ff6666']

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title("Log Severity Distribution")
    plt.axis("equal")
    plt.savefig("log_severity_pie_chart.png")
    print("🖼️ Pie chart saved as log_severity_pie_chart.png")
    plt.show()

# 📝 Save anomalies to a text file
def export_anomalies(anomalies, filename="anomalies_report.txt"):
    with open(filename, "w") as f:
        for entry in anomalies:
            f.write(entry + "\n")
    print(f"\n📝 Anomalies written to {filename}")

# 🧠 Check if the script is running in an interactive terminal
def is_interactive():
    return sys.stdin.isatty()

# 🚀 Main driver function
def main():
    print("\n🚀 Log Analyzer: Test Environment Deployment")
    print(f"🐍 Python Version: {platform.python_version()}")

    # 🤔 Optional severity filtering if interactive
    filter_level = None
    export_choice = "no"
    if is_interactive():
        severity_input = input("\n🔍 Enter severity to filter (INFO, WARNING, ERROR, or leave blank for all): ").strip().upper()
        filter_level = severity_input if severity_input else None
        export_choice = input("📝 Export anomalies to file? (yes/no): ").strip().lower()

    # 📂 Log file path
    log_file = "logs/sample_logs.txt"
    print(f"\n📄 Reading logs from: {log_file}")
    if not os.path.exists(log_file):
        print(f"❌ Log file not found: {log_file}")
        return

    with open(log_file, "r") as file:
        logs = file.readlines()

    # 🔍 Show filtered logs with line numbers
    display_logs_with_annotations(logs, filter_level)

    # 📊 Analyze log contents
    anomalies, severity_counts = analyze_logs(logs)

    print("\n🔹 Summary:")
    for level, count in severity_counts.items():
        print(f"- {level}: {count} entries")

    if anomalies:
        print("\n🚨 Anomalies Detected:")
        for entry in anomalies:
            print(f"  - {entry}")
        if export_choice == "yes":
            export_anomalies(anomalies)
    else:
        print("\n✅ No anomalies detected.")

    print("\n📈 Generating visualizations...")
    plot_severity_counts(severity_counts)
    plot_pie_chart(severity_counts)

# 🔁 Script entry point
if __name__ == "__main__":
    main()

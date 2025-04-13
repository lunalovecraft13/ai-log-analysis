# dev/app.py

import os
import sys
import platform
import matplotlib.pyplot as plt

# Function to analyze logs for anomalies and count severity levels
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

# Function to display the severity counts as a bar chart
def plot_severity_counts(severity_counts):
    labels = list(severity_counts.keys())
    counts = list(severity_counts.values())

    plt.figure(figsize=(6, 4))
    plt.bar(labels, counts, color="skyblue")
    plt.title("Log Severity Levels")
    plt.xlabel("Severity")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Main function to simulate test stage deployment
def main():
    print("🚀 Test environment deployment started...")
    print(f"🛠️ Python Version: {platform.python_version()}")
    
    log_file = "logs/sample_logs.txt"  # Update this path if your file is elsewhere

    print(f"\n📄 Reading logs from: {log_file}")
    if not os.path.exists(log_file):
        print(f"❌ Log file not found: {log_file}")
        return

    with open(log_file, "r") as f:
        logs = f.readlines()

    print("🔎 Detecting anomalies...")
    anomalies, severity_counts = analyze_logs(logs)

    if anomalies:
        print(f"⚠️ {len(anomalies)} anomalies detected:")
        for a in anomalies:
            print(f"  → {a}")
    else:
        print("✅ No anomalies detected.")

    # Show severity counts
    print("\n📊 Summary of log severities:")
    for level, count in severity_counts.items():
        print(f"  - {level}: {count} entries")

    # Plot chart
    plot_severity_counts(severity_counts)

    print("\n📦 Application Version: 1.0.1 (Test Stage Build)")
    print("✅ Log analysis complete. Test stage deployment successful.")

if __name__ == "__main__":
    main()

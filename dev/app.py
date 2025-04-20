# dev/app.py

import os
import platform
import matplotlib.pyplot as plt

# 🔌 Analyze logs for anomalies and count severity levels
# Takes a list of log lines and returns a list of anomalies and a dictionary of severity counts
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

# 🌈 Plot and save a bar chart of the severity counts
# Saves the chart as 'log_severity_summary.png' and also displays it visually
def plot_severity_counts(severity_counts):
    labels = list(severity_counts.keys())
    counts = list(severity_counts.values())

    plt.figure(figsize=(6, 4))
    plt.bar(labels, counts, color='orange')
    plt.title("Log Severity Levels")
    plt.xlabel("Severity")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("log_severity_summary.png")  # 📂 Save chart as image file
    plt.show()  # Display chart in a new window

# 🥧 Plot and save a pie chart of the severity distribution
# Saves the chart as 'log_severity_pie_chart.png'
def plot_pie_chart(severity_counts):
    labels = severity_counts.keys()
    sizes = severity_counts.values()
    colors = ['#66b3ff', '#ffcc99', '#ff6666']  # INFO, WARNING, ERROR

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Log Severity Distribution')
    plt.axis('equal')  # Makes the pie chart a circle
    plt.savefig("log_severity_pie_chart.png")  # 📂 Save pie chart as image
    print("🖼️ Pie chart saved as log_severity_pie_chart.png")
    plt.show()

# ⚙️ Main function that simulates the Test Stage
# Loads the logs, analyzes them, prints results, and generates charts
def main():
    print("\n🚀 Test environment deployment started...")
    print(f"⚒️ Python Version: {platform.python_version()}")

    # Define the path to the log file
    log_file = "logs/sample_logs.txt"
    print(f"\n📄 Reading logs from: {log_file}")

    # Check if the log file exists
    if not os.path.exists(log_file):
        print(f"❌ Log file not found: {log_file}")
        return

    # Read all lines from the log file
    with open(log_file, "r") as file:
        logs = file.readlines()

    print("🔎 Detecting anomalies...")
    anomalies, severity_counts = analyze_logs(logs)

    # Print a summary of severity levels
    print("\n🔹 Summary:")
    for level, count in severity_counts.items():
        print(f"- {level}: {count} entries")

    # Print details about any anomalies detected
    if anomalies:
        print("\n🚨 Anomalies Detected:")
        for entry in anomalies:
            print(f"  - {entry}")
    else:
        print("\n🚗 No anomalies detected.")

    print("\n📊 Log analysis complete. Test stage deployment successful.")

    # Generate and save the bar and pie charts
    plot_severity_counts(severity_counts)
    plot_pie_chart(severity_counts)

# 🔁 Entry point of the script
if __name__ == "__main__":
    main()

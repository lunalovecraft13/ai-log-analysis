# dev/app.py

import platform

# ✅ Define the function so test_app.py can import it
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


# 👇 Main script for running in the terminal or deployment simulation
if __name__ == "__main__":
    print("🚀 Test environment deployment started...")
    print(f"🔧 Python Version: {platform.python_version()}\n")

    log_file = "logs/sample_logs.txt"
    print(f"📄 Reading logs from: {log_file}")

    try:
        with open(log_file, 'r') as file:
            log_lines = file.readlines()
    except FileNotFoundError:
        print(f"❌ Log file not found: {log_file}")
        log_lines = []

    print("🔍 Detecting anomalies...")
    anomalies, counts = analyze_logs(log_lines)

    if anomalies:
        print("🚨 Anomalies detected:")
        for anomaly in anomalies:
            print(f" - {anomaly}")
    else:
        print("✅ No anomalies detected.")

    print("\n📊 Summary:")
    for level, count in counts.items():
        print(f" - {level}: {count} entries")

    print("\n🧪 Application Version: 1.0.0 (Test Stage Build)")
    print("✅ Log analysis complete. Test stage deployment successful.")

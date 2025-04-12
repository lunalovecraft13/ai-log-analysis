# dev/app.py

import platform
import re
import os

def analyze_logs(log_lines):
    """
    Returns a list of anomalies (lines with 'ERROR' or 'CRITICAL').
    """
    return [line.strip() for line in log_lines if 'ERROR' in line or 'CRITICAL' in line]

def read_log_file(filepath):
    """
    Reads log entries from a text file.
    """
    if not os.path.exists(filepath):
        print(f"❌ Log file not found: {filepath}")
        return []
    
    with open(filepath, 'r') as f:
        return f.readlines()

def main():
    print("🚀 Test environment deployment started...")
    print(f"🔧 Python Version: {platform.python_version()}\n")

    # Step 1: Load log entries
    log_file = "sample_logs.txt"  # or "logs/sample_logs.txt" if you use a folder
    print(f"📄 Reading logs from: {log_file}")
    raw_logs = read_log_file(log_file)

    # Step 2: Analyze the logs
    print("🧠 Detecting anomalies...\n")
    anomalies = analyze_logs(raw_logs)

    # Step 3: Print results
    if anomalies:
        print(f"❗ Anomalies Found ({len(anomalies)}):")
        for a in anomalies:
            print(f"   {a}")
    else:
        print("✅ No anomalies detected.")

    print("\n📦 Application Version: 1.0.0 (Test Stage Build)")
    print("✅ Log analysis complete. Test stage deployment successful.")

if __name__ == "__main__":
    main()

def main():
    print("🚀 Test environment deployment started...")
    print(f"🔧 Python Version: {platform.python_version()}\n")

    # Step 1: Load log entries
    log_file = "logs/sample_logs.txt"
    print(f"📄 Reading logs from: {log_file}")
    raw_logs = read_log_file(log_file)

    # Step 2: Analyze anomalies
    print("🧠 Detecting anomalies...\n")
    anomalies = analyze_logs(raw_logs)

    if anomalies:
        print(f"❗ Anomalies Found ({len(anomalies)}):")
        for a in anomalies:
            print(f"   {a}")
    else:
        print("✅ No anomalies detected.")

    # Step 3: Count log types
    severity_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    for line in raw_logs:
        for key in severity_counts:
            if key in line:
                severity_counts[key] += 1

    # Step 4: Print summary
    print("\n📊 Log Summary:")
    for level, count in severity_counts.items():
        print(f"- {level}: {count} entries")

    print("\n📦 Application Version: 1.0.0 (Test Stage Build)")
    print("✅ Log analysis complete. Test stage deployment successful.")

# dev/app.py

import re
import platform

# --- Step 1: Define a function to parse raw logs into structured data ---
def parse_logs(raw_logs):
    """
    Takes a list of raw log strings and returns structured dictionaries
    with extracted log level and message content.
    """
    parsed = []
    for line in raw_logs:
        # Use regular expression to capture log level and message
        match = re.match(r"\[(\w+)\].*?-\s+(.*)", line)
        if match:
            level = match.group(1)
            message = match.group(2)
            parsed.append({'level': level, 'message': message})
    return parsed

# --- Step 2: Define a function to detect anomalies ---
def detect_anomalies(log_entries):
    """
    Flags logs that are ERROR or CRITICAL level as anomalies.
    Returns a list of those flagged entries.
    """
    anomalies = []
    for entry in log_entries:
        if entry['level'] in ['ERROR', 'CRITICAL']:
            anomalies.append(entry)
    return anomalies

# --- Step 3: Simulate application behavior ---
def main():
    print("🚀 Test environment deployment started...")
    print(f"🔧 Python Version: {platform.python_version()}\n")

    # Simulated log entries (in real use, these could be from a file or cloud logs)
    raw_logs = [
        "[INFO] 2025-04-12 10:00:00 - Boot complete",
        "[ERROR] 2025-04-12 10:01:00 - Database connection failed",
        "[INFO] 2025-04-12 10:02:00 - Service started",
        "[CRITICAL] 2025-04-12 10:03:00 - Disk failure detected",
        "[WARN] 2025-04-12 10:04:00 - High memory usage"
    ]

    print("📄 Parsing logs...")
    structured_logs = parse_logs(raw_logs)

    print("🧠 Detecting anomalies...")
    anomalies = detect_anomalies(structured_logs)

    # --- Output Results ---
    if anomalies:
        print(f"\n❗ Anomalies Found ({len(anomalies)}):")
        for a in anomalies:
            print(f"   [{a['level']}] - {a['message']}")
    else:
        print("\n✅ No anomalies detected.")

    # --- Simulate versioning and deployment info ---
    print("\n📦 Application Version: 1.0.0 (Test Stage Build)")
    print("✅ Log analysis complete. Test stage deployment successful.")

# Run main() only if script is executed directly
if __name__ == "__main__":
    main()

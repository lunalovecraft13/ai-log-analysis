# dev/app.py

import re

# --- Simulation Kickoff ---
print("🚀 [TEST ENVIRONMENT] AI Log Analysis System launching...")
print("🧪 Running test-stage anomaly detection...")

# --- Sample log entries to simulate real data input ---
sample_logs = [
    "INFO 2025-04-12 10:00:00 User login successful",
    "ERROR 2025-04-12 10:01:00 Database connection failed",
    "INFO 2025-04-12 10:02:00 Response time: 105ms",
    "INFO 2025-04-12 10:03:00 Response time: 3120ms",  # High latency = anomaly
    "WARN 2025-04-12 10:04:00 Disk space at 85%",
    "ERROR 2025-04-12 10:05:00 Timeout while calling API"
]

# --- Define the anomaly detection function ---
def detect_anomalies(logs):
    flagged = []

    for line in logs:
        # Rule 1: Flag lines with the word "ERROR"
        if "ERROR" in line:
            flagged.append(f"🚨 Error Detected → {line}")

        # Rule 2: Flag lines with response times over 3000ms
        match = re.search(r"Response time: (\d+)ms", line)
        if match:
            response_time = int(match.group(1))
            if response_time > 3000:
                flagged.append(f"⚠️ High Latency → {line}")

    return flagged

# --- Run the detection and print the results ---
anomalies = detect_anomalies(sample_logs)

if anomalies:
    print("\n🔍 Anomalies Found:")
    for a in anomalies:
        print(f"   {a}")
else:
    print("✅ No anomalies detected.")

# --- Finish with a version log to simulate deployment logging ---
print("\n📦 App Version: 1.0.0 (Test Build)")
print("✅ Log analysis complete for Test environment.")

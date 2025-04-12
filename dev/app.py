# dev/app.py

import re

# Step 1: Confirm script is running
print("🚀 Test environment script is running...")

# Step 2: Simulated log entries (these could come from a file or API in the future)
sample_logs = [
    "INFO 2025-04-12 10:00:00 User login successful",
    "ERROR 2025-04-12 10:01:00 Database connection failed",
    "INFO 2025-04-12 10:02:00 Response time: 105ms",
    "INFO 2025-04-12 10:03:00 Response time: 3120ms",  # anomaly!
    "WARN 2025-04-12 10:04:00 Disk space at 85%",
    "ERROR 2025-04-12 10:05:00 Timeout while calling API"
]

# Step 3: Anomaly detection rules
def detect_anomalies(logs):
    flagged = []
    for line in logs:
        # Rule 1: Flag if "ERROR" is present
        if "ERROR" in line:
            flagged.append(f"🚨 ERROR detected: {line}")

        # Rule 2: Flag if response time exceeds 3000ms
        match = re.search(r"Response time: (\d+)ms", line)
        if match:
            response_time = int(match.group(1))
            if response_time > 3000:
                flagged.append(f"⚠️ High response time: {line}")

    return flagged

# Step 4: Run detection and display results
anomalies = detect_anomalies(sample_logs)

if anomalies:
    print("\n🔍 Anomalies detected:")
    for a in anomalies:
        print(a)
else:
    print("✅ No anomalies found in logs.")

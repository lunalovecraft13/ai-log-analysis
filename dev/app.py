# dev/app.py

"""
AI Log Analysis - Core Logic

This module provides basic log parsing functionality. 
It flags log lines as anomalies if they contain the keyword 'ERROR'.
"""

def analyze_logs(log_lines):
    """
    Analyze a list of log entries and detect anomalies.

    Args:
        log_lines (list): A list of strings, each representing a log entry.

    Returns:
        list: A list of log lines that are considered anomalies.
              Currently, any line containing the word 'ERROR' is flagged.
    """
    anomalies = []

    for line in log_lines:
        if 'ERROR' in line:
            anomalies.append(line)  # Flag line as an anomaly

    return anomalies


# Optional: You can run this file directly to test its output manually.
if __name__ == "__main__":
    sample_logs = [
        "INFO: System boot complete",
        "WARNING: CPU usage at 85%",
        "ERROR: Failed to initialize disk",
        "INFO: Monitoring active"
    ]

    flagged = analyze_logs(sample_logs)
    
    print("🚨 Detected Anomalies:")
    for line in flagged:
        print(line)

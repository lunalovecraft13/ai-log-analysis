import sys
import os
import unittest  # Python’s built-in unit testing framework

# 👇 Dynamically add the 'dev' directory to the Python path
# This ensures that 'app.py' in the 'dev' folder can be imported properly,
# even when the script is run from a different working directory (e.g., GitHub Actions).
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../dev')))

# 👇 Import the function to be tested from the app.py module
# We're assuming 'analyze_logs' exists in dev/app.py
from app import analyze_logs


# 👇 Define a test case by subclassing unittest.TestCase
class TestLogAnalyzer(unittest.TestCase):

    # 👇 This is a unit test function for the 'analyze_logs' function
    def test_detect_anomaly(self):
        # Provide sample log entries
        logs = [
            "INFO: All systems go",
            "ERROR: Disk space critically low",  # <-- This should be flagged as an anomaly
            "INFO: Still running"
        ]
        
        # Run the analyzer on the test logs
        anomalies = analyze_logs(logs)

        # Check that the known anomaly is in the results
        self.assertIn("ERROR: Disk space critically low", anomalies)


# 👇 Ensures this script runs the test when executed directly (not imported)
if __name__ == '__main__':
    unittest.main()

import sys
import os
import unittest  # Built-in unit testing framework

# 👇 Add 'dev' folder to the Python path so app.py can be imported from it
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../dev')))

# 👇 Import the function we want to test from app.py
from app import analyze_logs


# 👇 Define a test case class by extending unittest.TestCase
class TestLogAnalyzer(unittest.TestCase):

    # 👇 Test that known ERROR log is detected as an anomaly
    def test_detect_anomaly(self):
        logs = [
            "INFO: System boot complete",
            "ERROR: Disk space critically low",
            "INFO: Update check complete"
        ]
        anomalies, severity_counts = analyze_logs(logs)

        # ✅ Make sure the ERROR log was detected as an anomaly
        self.assertIn("ERROR: Disk space critically low", anomalies)

        # ✅ Also make sure severity count is correct (1 error, 2 info)
        self.assertEqual(severity_counts["ERROR"], 1)
        self.assertEqual(severity_counts["INFO"], 2)
        self.assertEqual(severity_counts["WARNING"], 0)

    # 👇 You can add more tests here if you want to expand coverage!
    # def test_detect_warning(self):
    #     ...


# 👇 Run the test only when this script is called directly
if __name__ == '__main__':
    unittest.main()

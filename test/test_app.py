import sys
import os
import unittest  # Python’s built-in testing framework

# === PATH SETUP =============================================================
# Ensure the 'dev' directory is in the system path so that 'app.py' can be imported
# This is especially useful when running tests via CI/CD environments like GitHub Actions

current_dir = os.path.dirname(__file__)                 # The directory this test file is in
dev_path = os.path.abspath(os.path.join(current_dir, '..', 'dev'))  # Path to 'dev/' folder
sys.path.insert(0, dev_path)                            # Add to import path

# === MODULE UNDER TEST ======================================================
# Now that the path is set up, import the function we want to test
from app import analyze_logs  # Assumes dev/app.py defines analyze_logs()


# === UNIT TESTS =============================================================
class TestLogAnalyzer(unittest.TestCase):
    """
    Unit tests for the log analysis functionality.
    """

    def test_detect_anomaly(self):
        """
        Test that 'analyze_logs' correctly identifies an error line as an anomaly.
        """
        sample_logs = [
            "INFO: All systems go",
            "ERROR: Disk space critically low",  # This should be flagged
            "INFO: Still running"
        ]

        result = analyze_logs(sample_logs)

        # Assert the expected anomaly is found
        self.assertIn("ERROR: Disk space critically low", result)


# === ENTRY POINT =============================================================
# This makes the test file executable directly: `python test_app.py`
if __name__ == '__main__':
    unittest.main()

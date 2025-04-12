# Import the unittest framework and the analyze_logs function from your app script
import unittest
from dev.app import analyze_logs  # Adjust path if needed

# Define a test case class for testing the log analysis function
class TestLogAnalysis(unittest.TestCase):

    # This test checks whether error logs are correctly detected from a sample list
    def test_detect_error_logs(self):
        # Sample logs: a mix of INFO, WARNING, and ERROR messages
        sample_logs = [
            "INFO: Boot complete",
            "ERROR: Database connection failed",
            "WARNING: High memory usage",
            "ERROR: Unauthorized access attempt"
        ]

        # Call the analyze_logs function with the sample logs
        results = analyze_logs(sample_logs)

        # There should be exactly 2 error logs detected
        self.assertEqual(len(results), 2)

        # The following specific error messages should be in the results
        self.assertIn("ERROR: Database connection failed", results)
        self.assertIn("ERROR: Unauthorized access attempt", results)

# This makes sure the tests run when the file is executed directly
if __name__ == '__main__':
    unittest.main()

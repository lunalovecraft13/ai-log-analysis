# test/test_app.py

# Import the function we want to test
from dev.app import detect_anomalies

# Test to ensure that error messages are correctly flagged
def test_detects_errors():
    logs = [
        "INFO Normal event",                      # Normal log (shouldn't be flagged)
        "ERROR Database failure"                  # Error log (should be flagged)
    ]
    result = detect_anomalies(logs)
    
    # Check that at least one flagged result contains "ERROR"
    assert any("ERROR" in line for line in result)

# Test to ensure that high response times are flagged as anomalies
def test_detects_high_latency():
    logs = [
        "INFO Response time: 999ms",              # Below threshold, not flagged
        "INFO Response time: 3200ms"              # Above threshold, should be flagged
    ]
    result = detect_anomalies(logs)
    
    # Check that at least one flagged result mentions response time
    assert any("response time" in line for line in result)
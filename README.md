# AI-Powered Log Analysis & Error Detection System

This project is an interactive command-line log analysis tool that uses Python to detect anomalies, filter by severity, generate visual reports, and export results. It is designed to simulate a "Test Stage" environment within a DevOps pipeline and can be easily extended for real-time monitoring or dashboard integration.

## 🔧 Features
- Reads structured log data from a file
- Annotated line-by-line log display with severity indicators
- Optional filtering by severity level (INFO, WARNING, ERROR)
- Anomaly detection for WARNING and ERROR logs
- Exports anomalies to `anomalies_report.txt`
- Bar and pie chart visualizations of log severity counts
- Interactive mode prompts only when run in a terminal

## 🧪 Technologies Used
- Python 3.11+
- Matplotlib (for charts)
- GitHub Actions (for CI/CD automation)

## 📂 Project Structure
```
├── dev/
│   └── app.py               # Main application script
├── logs/
│   └── sample_logs.txt      # Sample input log file
├── test/
│   └── test_app.py          # Unit tests for log analysis
├── .github/workflows/
│   └── promote-to-test.yml  # GitHub Actions CI script
├── log_severity_summary.png # Bar chart output
├── log_severity_pie_chart.png # Pie chart output
├── anomalies_report.txt     # Exported anomaly logs
├── requirements.txt         # Dependency file
```

## 🚀 Running the Application
1. Make sure Python and pip are installed.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python dev/app.py
   ```
4. (Optional) Pass a severity filter directly:
   ```bash
   python dev/app.py ERROR
   ```

## ✅ Sample Output
- Console log annotations with 🚨 symbols for warnings and errors
- Summary counts for each severity type
- Exported anomaly report if selected
- Saved visual charts in `.png` format

## 📦 Requirements
```
matplotlib
```

## 🤖 GitHub Actions (CI/CD)
The `promote-to-test.yml` workflow automates:
- Checking out code
- Setting up Python
- Installing dependencies
- Running `app.py` during push to main


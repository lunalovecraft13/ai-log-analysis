# 🔍 AI Log Analysis – DevOps Test Promotion Pipeline

Welcome to the **AI Log Analysis System** — a simulated DevOps environment designed to demonstrate CI/CD integration, automated testing, and anomaly detection in system logs using Python and GitHub Actions.

---

## 🚀 Project Summary

This project analyzes application logs to detect anomalies (e.g., error messages) and is set up with a **GitHub Actions workflow** to simulate promotion to a **Test Stage**. It includes:
- Log parsing and anomaly detection logic  
- Unit tests for validation  
- Automated GitHub workflow that installs dependencies, runs tests, and simulates deployment  

---

## 📁 File Structure




---

## 🧠 Features

- ✅ **Log Parsing**  
  Parses log messages line-by-line and identifies lines containing key anomalies (e.g., `ERROR`, `CRITICAL`).

- ✅ **Unit Testing**  
  Uses Python’s `unittest` to verify that anomaly detection works as expected.

- ✅ **CI/CD with GitHub Actions**  
  Automatically installs dependencies, runs tests, and simulates deployment on push to `main`.

---

## 🧪 Sample Log Anomaly Detection

The following logs:




Will detect:




---

## 🔨 Running the Code Locally

1. Clone the repository  
2. Navigate to the project directory  
3. Install dependencies:
   ```bash
   pip install -r requirements.txt



python dev/app.py



python -m unittest test/test_app.py

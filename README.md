# SSH Server Log Parser & Threat Detector
A Python tool to parse server logs and isolate brute-force threat actors

## 📌 Project Overview
This project is a lightweight Python script designed for security log analysis. It automates the process of parsing server logs, filtering out successful connection noise, and identifying potential threat actors attempting brute-force attacks.

## ⚙️ Features
* **Log Triage:** Strips and parses raw text logs into structured data blocks.
* **Failure Tracking:** Uses an internal scoring dictionary to track failed login counts per unique IP address.
* **Threat Identification:** Detects malicious activity dynamically if an IP address crosses a threshold of 3 or more failed attempts.
* **Report Generation:** Automatically outputs threat intelligence data directly into a structured `threat_report.csv` file for firewall blocking.

## 🛠️ How It Works
The core logic utilizes a list comprehension to dynamically extract specific attacker information when a threshold breach is detected:
```python
attacker_info = [Info for Info in Data if Info["IP"] == ip][0]
rsta.writerow(attacker_info)

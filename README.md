# Advanced Network Intrusion Detection System (IDS)

## Overview

The Advanced Network Intrusion Detection System (IDS) is a Python-based cybersecurity project designed to monitor network traffic, detect suspicious activities, and generate security alerts in real time. The system combines packet analysis, threat detection, threat intelligence, ransomware activity monitoring, alert logging, and incident reporting to provide a comprehensive security monitoring solution.

## Features

### Network Traffic Monitoring

* Captures live network packets using Scapy.
* Identifies source IP, destination IP, and protocol information.

### Port Scan Detection

* Detects potential reconnaissance activities by monitoring connections to multiple ports from the same source IP.

### ICMP Flood Detection

* Detects excessive ICMP packets that may indicate a flooding attack.

### DNS Abuse Detection

* Monitors DNS requests and identifies excessive or suspicious DNS queries.

### Threat Intelligence Integration

* Compares observed IP addresses against a blacklist feed.
* Generates alerts when communication with blacklisted IPs is detected.

### Brute Force Detection

* Analyzes authentication logs for repeated failed login attempts.
* Detects potential brute-force attacks.

### Ransomware Activity Detection

* Monitors file system activity.
* Detects rapid file modifications that may indicate ransomware behavior.

### Alert Management

* Generates alerts with severity levels:

  * LOW
  * MEDIUM
  * HIGH
  * CRITICAL

### Alert Logging

* Stores all generated alerts in `alerts.log` for future analysis.

### Real-Time Dashboard

* Flask-based web dashboard displaying:

  * Total Alerts
  * Critical Alerts
  * High Alerts
  * Medium Alerts
  * Threat Intelligence Alerts
  * Recent Security Events

### PDF Incident Reports

* Automatically generates PDF reports summarizing detected incidents and security statistics.

---

## Technologies Used

* Python
* Scapy
* Flask
* Watchdog
* ReportLab
* Threading
* SMTP (Email Alerts)
* HTML/CSS

---

## Project Structure

```text
Network_IDS/
│
├── main.py
├── capture.py
├── alert.py
├── alert_store.py
├── logger.py
├── dashboard.py
├── port_scan.py
├── icmp_flood.py
├── dns_detector.py
├── threat_intel.py
├── brute_force.py
├── log_analyzer.py
├── ransomware_detector.py
├── report_generator.py
├── email_alert.py
├── blacklist.txt
├── alerts.log
├── incident_report.pdf
|── requirements.txt

```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd Network_IDS
```

2. Create virtual environment

```bash
python -m venv venv
```

3. Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Start the IDS:

```bash
python main.py
```

Dashboard:

```text
http://127.0.0.1:5000
```

---

## Dashboard Features

* Live Alert Monitoring
* Alert Statistics
* Threat Intelligence Tracking
* Security Event Visualization


---

## Sample Alerts

```text
[HIGH] Port Scan Detected

[CRITICAL] Blacklisted IP Detected

[HIGH] Brute Force Attack Detected

[CRITICAL] Possible Ransomware Activity Detected
```

---

## Future Enhancements

* Machine Learning Based Threat Detection
* GeoIP Attack Mapping
* SIEM Integration
* External Threat Intelligence Feeds
* Real-Time Email Notifications
* Attack Timeline Visualization
* REST API Integration

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Network Traffic Analysis
* Intrusion Detection Systems
* Threat Intelligence
* Security Monitoring
* Python Automation
* Flask Web Development
* Incident Reporting
* Cybersecurity Operations

---

## Author

Khushi Singh

B.Tech Computer Science Engineering (Cyber Security)

Manipal Academy of Higher Education, Bengaluru

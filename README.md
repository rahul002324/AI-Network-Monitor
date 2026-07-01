# 🛡️ Smart IDS AI
### AI-Powered Intrusion Detection System for Network Monitoring

Smart IDS AI is an intelligent Intrusion Detection System (IDS) built using Python. It monitors live network traffic, detects suspicious activities using rule-based detection and machine learning, logs network packets, generates alerts, and provides a professional terminal-based dashboard for monitoring network security.

---

## 🚀 Features

- 📡 Real-time Packet Sniffing using Scapy
- 🛡️ Rule-Based Attack Detection
  - Port Scan Detection
  - Suspicious Traffic Detection
- 🤖 AI-Based Anomaly Detection (Isolation Forest)
- 📊 Live Network Traffic Monitoring
- 📁 Automatic Daily Traffic Logging (CSV)
- 📁 Attack Log Generation
- 📧 Email Alerts for Detected Attacks
- 🔥 Windows Firewall IP Blocking
- 📋 View Blocked IP Addresses
- 🖥️ Professional Interactive CLI Dashboard
- 🧹 Automatic Cleanup of Old Log Files
- 📈 AI Model Training from Captured Traffic

---

# 📂 Project Structure

```
Smart IDS AI/
│
├── capture/
│   └── packet.py             # Packet capture & logging
│
├── detection/
│   ├── rule.py               # Rule-based detection
│   ├── ai.py                 # AI anomaly detection
│   └── model.pkl             # Trained AI model
│
├── response/
│   ├── autoresponse.py       # Firewall block & unblock
│   └── email.py              # Email notifications
│
├── data/
│   ├── YYYY-MM-DD.csv        # Daily traffic logs
│   ├── attacks_YYYY-MM-DD.csv# Attack logs
│   └── blocked_ips.csv       # Blocked IP records
│
├── smartids.py               # Interactive terminal dashboard
├── main.py                   # IDS Engine
└── README.md
```

---

# ⚙️ Technologies Used

- Python 3
- Scapy
- Pandas
- Scikit-Learn
- Rich
- PyFiglet
- SMTP
- Windows Firewall (netsh)

---

# 🧠 Detection Techniques

## Rule-Based Detection

Current rules include:

- Port Scan Detection
- Suspicious Connection Monitoring
- Custom Detection Rules

---

## AI-Based Detection

Smart IDS AI uses the **Isolation Forest** algorithm to identify abnormal network traffic.

Features used:

- Destination Port
- Packet Size

The AI model is automatically trained using captured traffic logs.

---

# 📊 Logging

Every captured packet is stored in a daily CSV file.

Example:

```
data/
├── 2026-06-12.csv
```

Detected attacks are stored separately.

```
attacks_2026-06-12.csv
```

---

# 📧 Email Alert

Whenever a suspicious activity is detected, Smart IDS AI can automatically send an email notification containing:

- Attack Type
- Attacker IP
- Severity
- Timestamp

---

# 🚫 Firewall Response

The system can automatically block malicious IP addresses using Windows Firewall.

Blocked IPs can also be viewed from the Smart IDS dashboard.

---

# 🖥️ Smart IDS Terminal

Launch the interactive dashboard:

```bash
python smartids.py
```

Commands

| Command | Description |
|----------|-------------|
| help | Show available commands |
| start | Start IDS Engine |
| traffic | Show recent captured traffic |
| attacks | Show detected attacks |
| blocked | View blocked IPs |
| clear | Clear screen |
| exit | Exit Smart IDS |

---

# ▶️ Running the Project

Clone the repository

```bash
git clone https://github.com/rahul002324/AI-Network-Monitor.git
```

Move into the project

```bash
cd AI-Network-Monitor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Smart IDS

```bash
python smartids.py
```

---

# 📌 Current Capabilities

✅ Live Packet Capture

✅ Rule-Based Detection

✅ AI Anomaly Detection

✅ Attack Logging

✅ Daily Traffic Logging

✅ Email Alerts

✅ Windows Firewall Integration

✅ Interactive CLI Dashboard

---

# 🚀 Future Improvements

- Web Dashboard
- Honeypot Integration
- Threat Intelligence API
- IP Reputation Lookup
- Malware Signature Detection
- AI Retraining Automation
- Real-Time Graphs
- Multi-Platform Firewall Support
- Database Storage
- PDF Security Reports

---

# 👨‍💻 Author

**Rahul R**

Cybersecurity Enthusiast

GitHub:
https://github.com/rahul002324

---

# 📜 License

This project is licensed under the MIT License.

---

⭐ If you like this project, consider giving it a Star on GitHub!

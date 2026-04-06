# 🔐 SSH Brute Force Detector

A Python-based cybersecurity tool that detects **SSH brute-force attacks** by analyzing authentication logs.

The tool parses SSH login logs, detects suspicious IP addresses based on repeated failed login attempts, and generates a security report. It can also monitor logs in **real-time**, acting as a simple **Intrusion Detection System (IDS)**.

---

## 🚀 Features

* 📄 Parse SSH authentication logs
* 🚨 Detect brute-force login attempts
* 🌍 Identify suspicious IP addresses
* 📊 Rank attackers by number of attempts
* 👀 Real-time log monitoring (mini IDS)

---

## 🏗 Architecture
```
                 ┌───────────────────┐
                 │   SSH Log File    │
                 └─────────┬─────────┘
                           │
                           ▼
                ┌───────────────────┐
                │   log_parser.py   │
                │  Extract events   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ attack_detector.py│
                │ Detect attackers  │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │report_generator.py│
                │ Security report   │
                └─────────┬─────────┘
                          │
                          ▼
                    User Output


Optional Real-Time Monitoring Mode
----------------------------------

                 ┌───────────────────┐
                 │     monitor.py    │
                 │  Watches log file│
                 └─────────┬─────────┘
                           │
                           ▼
                    SSH Log File
                           │
                           ▼
                    log_parser.py
                           │
                           ▼
                  attack_detector.py
                           │
                           ▼
                 report_generator.py
                           │
                           ▼
                      Live Alerts
```

---

## 🗂 Project Structure

```
ssh-bruteforce-detector
│
├── logs
│   └── sample_auth.log        # Example SSH log file used for testing
│
├── src
│   ├── analyzer.py            # Main CLI tool that runs analysis
│   ├── log_parser.py          # Extracts events (timestamp, IP) from logs
│   ├── attack_detector.py     # Detects brute-force attacks based on thresholds
│   ├── report_generator.py    # Generates formatted security reports
│   ├── monitor.py             # Real-time log monitoring (mini IDS)
│   └── utils.py               # Helper functions shared across modules
│
├── tests
│   └── test_parser.py         # Unit tests for log parsing functionality
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── LICENSE                    # Open-source license
└── .gitignore                 # Ignore cache files, environment files, etc
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/navanil-das/ssh-bruteforce-detector.git
cd ssh-bruteforce-detector
```

---

## ▶️ Usage

Run log analysis:

```bash
py src/analyzer.py logs/sample_auth.log
```

Run real-time monitoring:

```bash
py src/analyzer.py logs/sample_auth.log --monitor
```

---

## 📈 Example Output

```
SSH Brute Force Detection Report
--------------------------------

Top Attackers

1. 192.168.1.10 → 7 failed attempts
2. 192.168.1.45 → 3 failed attempts
```

---

## 🛡 Cybersecurity Concepts Used

* Log analysis
* Intrusion detection
* Security monitoring
* Automation scripting

---

## 📚 Future Improvements

* 🔒 Automatic IP blocking (Fail2Ban-style)
* 📊 Attack timeline visualization
* 📧 Email alerts for detected attacks
* ⚡ Faster log monitoring

---

## 👨‍💻 Author

**Navanil Das**

- GitHub: [https://github.com/navanil-das](https://github.com/navanil-das)
- LinkedIn: [https://linkedin.com/in/navanil-das](https://www.linkedin.com/in/navanil-das-83ba41296/)

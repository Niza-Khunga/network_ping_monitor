# 🌐 Network Ping Monitor with Alerting (Python)

A lightweight Python tool for monitoring host reachability using ICMP ping. Built as part of a personal **“1 project per day”** learning challenge to strengthen scripting, logging, testing, and network engineering fundamentals.

Designed by a Trainee Software Engineer training in **Core Network Engineering** at a telecom company.

---

## 🎯 Features

* **Cross-platform support**: Works on Windows, Linux, and macOS
* **Automatic logging**: Saves ping results with timestamps to `ping_log.txt`
* **Unit tested**: Includes basic tests using `pytest`
* **Easily extendable**: Add more hosts directly in the script

---

## 🛠️ Tech Stack

* **Python**: 3.7+
* **Built-ins**: `subprocess`, `logging`, `platform`
* **Testing**: `pytest`
* **Tools used**: VS Code, Git, GitHub

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/network-ping-monitor.git
cd network-ping-monitor
```

### 2. Install test dependencies

```bash
pip install pytest
```

### 3. Run the monitor

```bash
python ping_monitor.py
```

> Default hosts: `127.0.0.1` (localhost) and `8.8.8.8` (Google DNS).
> Edit the `hosts` list in `ping_monitor.py` to add your own IPs.

### 4. Run tests

```bash
pytest -v
```

---

## 📂 Project Structure

```
network-ping-monitor/
├── ping_monitor.py        # Main script
├── test_ping_monitor.py   # Unit tests
├── ping_log.txt           # Auto-generated log file (ignored by Git)
├── .gitignore
└── README.md
```

---

## 🧪 Testing Overview

This project uses **pytest** to validate core functionality:

* **`test_localhost`** → Confirms that a known reachable host (`127.0.0.1`) returns `True`
* **`test_invalid_host`** → Ensures unreachable IPs correctly return `False`

> Testing with `127.0.0.1` prevents flaky tests caused by corporate or telecom network restrictions, ensuring reliable runs.

---

## 🎓 Learning Outcomes

* Built a cross-platform network utility
* Implemented structured logging
* Wrote foundational Python unit tests
* Handled OS-specific command differences
* Published a complete, documented project to GitHub 🎉

---

## 🌱 Future Enhancements

* Email/SMS alerts when a host becomes unreachable
* Continuous background service mode
* Web-based dashboard (React/Express)
* Persist results to a database—or explore blockchain logging

---

## 🙌 About the Author

Trainee Software Engineer and Computer Science graduate, currently interning at a Telecom Company and training towards becoming a ****Core Network Engineer**.**
Building one project per day to strengthen programming, testing, and system engineering skills.

🔗 GitHub: [https://github.com/](https://github.com/Niza-Khunga) 
📧 *[nizahkhunga@gmail.com](mailto:nizaahkhunga@gmail.com)*

---

> ✨ *“The best way to learn is to build, break, fix, and share.”*

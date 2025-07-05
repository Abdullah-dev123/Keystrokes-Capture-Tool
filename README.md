# 🔐 Keystrokes-Capture-Tool (Educational Project)

This project is a **basic keylogger built with Python**, using the `pynput` library.  
It captures user keystrokes and sends them to a server using sockets.

🚨 **This tool is created solely for educational and ethical hacking purposes. Do not use it maliciously.**

---

## ⚙️ Features

- Logs all key presses (including special keys like Enter, Shift, etc.)
- Sends keystrokes over TCP to a remote server
- Saves logs in a text file
- Clean and minimal code — great for beginners

---

## 🚀 How It Works

1. `client.py`: Captures keystrokes and sends them to the specified server
2. `server.py`: Listens for incoming connections and writes logs to `logs.txt`

---

## 🧠 Requirements

- Python 3.x
- `pynput` library  
  Install it using:
  ```bash
  pip install pynput

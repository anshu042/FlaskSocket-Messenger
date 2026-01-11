# 💬 Multi-User Chat Room & Messaging Platform

![Project Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.2.2-lightgrey)
![Firebase](https://img.shields.io/badge/Database-Firebase_Firestore-orange)

A robust, real-time secure instant messaging platform built with **Python Flask**, **Socket.IO**, and **Google Firebase**. This application features a modern "Dark Glass" UI, secure user authentication, and persistent cloud-based message storage.

---

## 🌟 Features

* **⚡ Real-time Messaging:** Bi-directional low-latency communication using WebSockets (`Flask-SocketIO`).
* **🔒 Secure Authentication:** Custom Signup and Login system utilizing `PBKDF2 SHA256` password hashing.
* **☁️ Cloud Persistence:** All user data and chat history are securely stored in **Google Cloud Firestore**, ensuring data isn't lost on server restarts.
* **👥 Private Chat Rooms:** Initiate private conversations with other users via email invitations.
* **🛠️ Chat Management:**
    * **Clear History:** Instantly delete all messages in a specific chat room.
    * **Remove Chat:** Hide users from your active sidebar without deleting history.
* **🎨 Modern UI:** A responsive, glassmorphism-inspired interface ("Dark Glass") with a split-pane design.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python, Flask | Core application server framework. |
| **WebSockets** | Flask-SocketIO | Handles real-time events and message broadcasting. |
| **Database** | Firebase Firestore | NoSQL cloud database for storing Users, Rooms, and Messages. |
| **Frontend** | HTML5, CSS3, JS | Custom responsive UI with Socket.IO client integration. |
| **Server** | Gunicorn + Eventlet | Production-ready WSGI/ASGI server configuration. |

---

## 📂 Project Structure

```text
multi-user-chat-room/
├── instance/              # Instance specific config
├── myapp/
│   ├── static/            # CSS (auth.css, chat.css), JS, and Images
│   ├── templates/         # HTML Templates (auth.html, chat.html)
│   ├── __init__.py        # App factory and Flask extension initialization
│   ├── config.py          # Environment configuration
│   ├── database.py        # Firebase Firestore initialization
│   └── views.py           # Application routes and Auth logic
├── .env                   # Environment variables (Secret Keys)
├── gunicorn_config.py     # Gunicorn production config
├── requirements.txt       # Python dependencies
├── server.py              # Application entry point
└── vercel.json            # Deployment configuration
```

## 🖥️ Preview
<img width="1919" height="1038" alt="FlaskSocket-Preview01" src="https://github.com/user-attachments/assets/998b0800-48b3-4b71-9600-a9e0f40aa62d" />
<img width="1919" height="1037" alt="FlaskSocket-Preview02" src="https://github.com/user-attachments/assets/063c9c9d-5c23-4756-8961-0a38574f4636" />
<img width="1919" height="1034" alt="FlaskSocket-Preview03" src="https://github.com/user-attachments/assets/6b39c8f5-dde4-41d2-8d6e-afa1bbac098b" />
<img width="1918" height="997" alt="FlaskSocket-Preview04" src="https://github.com/user-attachments/assets/04de44fd-9d18-4cfb-afc1-3e8759d6b192" />

<div align="center">
  
## 📫 Connect With Me

[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:anshu04232@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/anshu042)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/anshhu04)

**Anshu Kushwaha**

</div>

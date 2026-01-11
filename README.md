# Secure Instant Messaging Platform - FlaskSocket Messenger

A real-time chat application built with **Flask**, **Socket.IO**, and **SQLAlchemy**. This application allows users to register, create private chat rooms, and exchange instant messages with a modern "Dark Glass" UI.

## 🚀 Features

* **Real-time Messaging:** Instant bi-directional communication using WebSockets (Flask-SocketIO).
* **User Authentication:** Secure Signup and Login system with password hashing (PBKDF2 SHA256).
* **Private Chat Rooms:** Create distinct chat rooms between users via email invitation.
* **Persistent Chat History:** Messages are stored in a SQLite database and retrieved upon loading the chat.
* **Chat Management:**
    * Clear chat history for a specific room.
    * Remove chats/users from your sidebar.
* **Modern UI:** Custom CSS featuring a responsive split-pane login and a glassmorphism-styled chat interface.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **WebSockets:** Flask-SocketIO
* **Database:** SQLite (Default), SQLAlchemy ORM
* **Frontend:** HTML5, CSS3, JavaScript (Socket.IO client, jQuery)
* **Server:** Gunicorn (Configuration provided)

## 📂 Project Structure

```text
FlaskSocket-Messenger/
├── myapp/
│   ├── __init__.py          # App factory and DB initialization
│   ├── config.py            # App configuration variables
│   ├── database.py          # Database models (User, Chat, Message)
│   ├── views.py             # HTTP routes (Auth, Chat logic)
│   ├── static/              # CSS, JS, and Images
│   └── templates/           # HTML Templates (auth.html, chat.html, etc.)
├── instance/
│   └── database.db          # SQLite Database (generated on run)
├── .env                     # Environment variables
├── gunicorn_config.py       # Production server config
├── requirements.txt         # Python dependencies
└── server.py                # Application entry point
```

## 📖 Usage

- **Register:** Create a new account using the "Signup" form.
- **Login:** Log in with your credentials.
- **Start a Chat:**
    * Click the "New Chat" button.
    * Enter the email address of another registered user.
- **Chat:** Select the user from the sidebar and start typing. Messages will appear instantly.
- **Options:** Use the three-dot menu (⋮) next to a user in the sidebar to **Clear Chat** or **Remove User**.

## 🔜 Future Improvements
- **Profile Management:** Allow users to update their avatars and bio.
- **Group Chats:** Extend functionality to support multi-user rooms.

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

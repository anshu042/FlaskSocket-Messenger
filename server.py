# 1. LOAD ENVIRONMENT VARIABLES FIRST
from dotenv import load_dotenv
load_dotenv() 

# 2. NOW IMPORT YOUR APP
from myapp import create_app
from myapp.database import db
from flask_socketio import emit, join_room, leave_room
from firebase_admin import firestore

app, socket = create_app()

@socket.on("join-chat")
def join_private_chat(data):
    room = data["rid"]
    join_room(room=room)
    socket.emit(
        "joined-chat",
        {"msg": f"{room} is now online."},
        room=room,
    )

@socket.on("outgoing")
def chatting_event(json, methods=["GET", "POST"]):
    room_id = json["rid"]
    timestamp = json["timestamp"]
    message = json["message"]
    sender_id = json["sender_id"]
    sender_username = json["sender_username"]

    message_data = {
        'content': message,
        'timestamp': timestamp,
        'sender_id': sender_id,
        'sender_username': sender_username,
        'room_id': room_id,
    }

    try:
        # Save to Firebase
        db.collection('rooms').document(room_id).collection('messages').add(message_data)
    except Exception as e:
        print(f"Error saving message to database: {str(e)}")

    socket.emit(
        "message",
        json,
        room=room_id,
        include_self=False,
    )

if __name__ == "__main__":
    socket.run(app, allow_unsafe_werkzeug=True, debug=True)
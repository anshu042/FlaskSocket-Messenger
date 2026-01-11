from flask import Blueprint, render_template, request, url_for, redirect, session, flash, jsonify
from myapp.database import db
from functools import wraps
from passlib.hash import pbkdf2_sha256
from myapp import socket
from datetime import datetime
import pandas as pd
import io
import base64
# --- ADDED THIS MISSING IMPORT ---
from firebase_admin import firestore 

views = Blueprint('views', __name__, static_folder='static', template_folder='templates')

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("views.login"))
        return f(*args, **kwargs)
    return decorated

@views.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for("views.login"))

@views.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        username = request.form["username"].strip().lower()
        password = request.form["password"]

        users_ref = db.collection('users')
        query = users_ref.where('username', '==', username).get()
        
        if len(query) > 0:
            flash("User already exists with that username.")
            return redirect(url_for("views.login"))

        hashed_password = pbkdf2_sha256.hash(password)
        
        new_user = {
            'username': username,
            'email': email,
            'password': hashed_password,
            'date': datetime.utcnow(),
            'chat_list': []
        }
        
        db.collection('users').add(new_user)

        flash("Registration successful.")
        return redirect(url_for("views.login"))

    return render_template("auth.html")

@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        users_ref = db.collection('users')
        results = users_ref.where('email', '==', email).limit(1).get()

        user_data = None
        user_id = None
        
        for doc in results:
            user_data = doc.to_dict()
            user_id = doc.id

        if user_data and pbkdf2_sha256.verify(password, user_data['password']):
            session["user"] = {
                "id": user_id,
                "username": user_data['username'],
                "email": user_data['email'],
            }
            return redirect(url_for("views.chat"))
        else:
            flash("Invalid login credentials. Please try again.")
            return redirect(url_for("views.login"))

    return render_template("auth.html")

@views.route("/new-chat", methods=["POST"])
@login_required
def new_chat():
    user_id = session["user"]["id"]
    new_chat_email = request.form["email"].strip().lower()

    if new_chat_email == session["user"]["email"]:
        return redirect(url_for("views.chat"))

    users_ref = db.collection('users')
    recipient_query = users_ref.where('email', '==', new_chat_email).limit(1).get()
    
    recipient_id = None
    recipient_data = None
    
    for doc in recipient_query:
        recipient_id = doc.id
        recipient_data = doc.to_dict()

    if not recipient_id:
        return redirect(url_for("views.chat"))

    user_ref = db.collection('users').document(user_id)
    user_doc = user_ref.get().to_dict()
    
    current_chat_list = user_doc.get('chat_list', [])
    
    recipient_in_list = False
    for chat in current_chat_list:
        if chat['user_id'] == recipient_id:
            recipient_in_list = True
            break
            
    if not recipient_in_list:
        room_id = "_".join(sorted([user_id, recipient_id]))
        
        current_chat_list.append({"user_id": recipient_id, "room_id": room_id})
        user_ref.update({'chat_list': current_chat_list})
        
        recipient_ref = db.collection('users').document(recipient_id)
        recipient_doc = recipient_ref.get().to_dict()
        recipient_chat_list = recipient_doc.get('chat_list', [])
        
        recipient_has_chat = False
        for r_chat in recipient_chat_list:
            if r_chat['user_id'] == user_id:
                recipient_has_chat = True
                break
                
        if not recipient_has_chat:
            recipient_chat_list.append({"user_id": user_id, "room_id": room_id})
            recipient_ref.update({'chat_list': recipient_chat_list})

    return redirect(url_for("views.chat"))

@views.route("/chat/", methods=["GET", "POST"])
@login_required
def chat():
    room_id = request.args.get("rid", None)
    current_user_id = session["user"]["id"]
    
    user_doc = db.collection('users').document(current_user_id).get().to_dict()
    chat_list = user_doc.get('chat_list', [])

    data = []

    for chat_item in chat_list:
        other_user_doc = db.collection('users').document(chat_item["user_id"]).get()
        if other_user_doc.exists:
            other_user_data = other_user_doc.to_dict()
            username = other_user_data.get('username')
            is_active = room_id == chat_item["room_id"]
            
            messages_ref = db.collection('rooms').document(chat_item["room_id"]).collection('messages')
            # Now this line will work because firestore is imported
            last_msg_query = messages_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1).get()
            
            last_message_content = "This place is empty. No messages ..."
            for msg in last_msg_query:
                last_message_content = msg.to_dict().get('content', '')

            data.append({
                "username": username,
                "room_id": chat_item["room_id"],
                "is_active": is_active,
                "last_message": last_message_content,
            })

    messages = []
    if room_id:
        messages_ref = db.collection('rooms').document(room_id).collection('messages')
        all_msgs = messages_ref.order_by('timestamp').stream()
        for msg in all_msgs:
            messages.append(msg.to_dict())

    return render_template(
        "chat.html",
        user_data=session["user"],
        room_id=room_id,
        data=data,
        messages=messages,
    )

@views.app_template_filter("ftime")
def ftime(date):
    try:
        dt = datetime.fromtimestamp(int(date))
        time_format = "%I:%M %p" 
        formatted_time = dt.strftime(time_format)
        formatted_time += " | " + dt.strftime("%m/%d")
        return formatted_time
    except:
        return ""

@views.route('/visualize')
def visualize():
    pass

@views.route('/get_name')
def get_name():
    data = {'name': ''}
    if 'username' in session:
        data = {'name': session['username']}
    return jsonify(data)

@views.route('/get_messages')
def get_messages():
    pass

@views.route('/leave')
def leave():
    session.clear()
    return redirect(url_for('views.login'))

@views.route('/remove_chat/<room_id>')
@login_required
def remove_chat(room_id):
    current_user_id = session["user"]["id"]
    user_ref = db.collection('users').document(current_user_id)
    user_doc = user_ref.get().to_dict()
    
    if user_doc:
        chat_list = user_doc.get('chat_list', [])
        updated_list = [c for c in chat_list if c['room_id'] != room_id]
        user_ref.update({'chat_list': updated_list})

    return redirect(url_for('views.chat'))

@views.route('/clear_chat/<room_id>')
@login_required
def clear_chat(room_id):
    try:
        messages_ref = db.collection('rooms').document(room_id).collection('messages')
        docs = messages_ref.stream()
        for doc in docs:
            doc.reference.delete()
    except Exception as e:
        print(f"Error clearing chat: {e}")

    return redirect(url_for('views.chat', rid=room_id))
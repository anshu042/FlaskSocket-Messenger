import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

if not firebase_admin._apps:
    try:
        cred_json = os.environ.get('FIREBASE_CREDENTIALS')
        if cred_json:
            cred_dict = json.loads(cred_json)
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
        else:
            print("Warning: FIREBASE_CREDENTIALS environment variable not found.")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")

db = firestore.client()
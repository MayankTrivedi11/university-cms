import json
from uuid import uuid4
from config import Config
from helpers import auth_helper
import threading

ledger_lock = threading.Lock()

def register_user(data):
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r+') as f:
            ledger_data = json.load(f)
            users = ledger_data.get('users', [])

            # Check if user already exists (by email)
            if any(user['email'] == data['email'] for user in users):
                raise ValueError("User with this email already exists")

            user_id = str(uuid4())
            hashed_password = auth_helper.hash_password(data['password'])
            new_user = {
                'id': user_id,
                'name': data['name'],
                'email': data['email'],
                'password': hashed_password  # Store the hashed password
            }

            users.append(new_user)
            ledger_data['users'] = users
            f.seek(0)
            json.dump(ledger_data, f, indent=4)
            f.truncate()
            return new_user

def login_user(data):
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r') as f:
            ledger_data = json.load(f)
            users = ledger_data.get('users', [])

            user = next((user for user in users if user['email'] == data['email']), None)

            if user and auth_helper.verify_password(data['password'], user['password']):
                # Generate a token (e.g., JWT).  For now, just return a dummy token.
                token = auth_helper.generate_token(user['id'])  # Replace with JWT generation
                return token
            else:
                raise ValueError("Invalid credentials")
                
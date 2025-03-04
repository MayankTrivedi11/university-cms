import bcrypt
import jwt
from datetime import datetime, timedelta
from config import Config

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Store as a string

def verify_password(password, hashed_password):
    # Check if the password matches the hash
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def generate_token(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),  # Token expires in 1 day
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload['sub']  # Returns the user ID
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token
        
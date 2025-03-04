from flask import jsonify, request
from services import auth_service
from validators import auth_validator

def register(data):
    errors = auth_validator.validate_registration(data)
    if errors:
        return jsonify({'errors': errors}), 400

    try:
        user = auth_service.register_user(data)
        return jsonify({'message': 'User registered successfully', 'user_id': user['id']}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

def login(data):
    errors = auth_validator.validate_login(data)
    if errors:
        return jsonify({'errors': errors}), 400

    try:
        token = auth_service.login_user(data)
        return jsonify({'token': token}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 401
        
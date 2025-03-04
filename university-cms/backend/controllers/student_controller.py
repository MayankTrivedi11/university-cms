from flask import jsonify, request
from services import student_service
from validators import student_validator

def get_all_students():
    students = student_service.get_all_students()
    return jsonify(students), 200

def get_student(student_id):
    student = student_service.get_student(student_id)
    if student:
        return jsonify(student), 200
    return jsonify({'message': 'Student not found'}), 404

def create_student(data):
    errors = student_validator.validate_student(data)
    if errors:
        return jsonify({'errors': errors}), 400

    new_student = student_service.create_student(data)
    return jsonify(new_student), 201

def update_student(student_id, data):
    errors = student_validator.validate_student(data)
    if errors:
        return jsonify({'errors': errors}), 400

    updated_student = student_service.update_student(student_id, data)
    if updated_student:
        return jsonify(updated_student), 200
    return jsonify({'message': 'Student not found'}), 404

def delete_student(student_id):
    if student_service.delete_student(student_id):
        return jsonify({'message': 'Student deleted'}), 200
    return jsonify({'message': 'Student not found'}), 404
    
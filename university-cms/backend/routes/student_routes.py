from flask import Blueprint, request, jsonify
from controllers import student_controller

student_bp = Blueprint('students', __name__, url_prefix='/students')

@student_bp.route('/', methods=['GET'])
def get_all_students():
    return student_controller.get_all_students()

@student_bp.route('/<student_id>', methods=['GET'])
def get_student(student_id):
    return student_controller.get_student(student_id)

@student_bp.route('/', methods=['POST'])
def create_student():
    return student_controller.create_student(request.get_json())

@student_bp.route('/<student_id>', methods=['PUT'])
def update_student(student_id):
    return student_controller.update_student(student_id, request.get_json())

@student_bp.route('/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    return student_controller.delete_student(student_id)
    
from flask import Blueprint, request, jsonify
from controllers import course_controller

course_bp = Blueprint('courses', __name__, url_prefix='/courses')

@course_bp.route('/', methods=['GET'])
def get_all_courses():
    return course_controller.get_all_courses()

@course_bp.route('/<course_id>', methods=['GET'])
def get_course(course_id):
    return course_controller.get_course(course_id)

@course_bp.route('/', methods=['POST'])
def create_course():
    return course_controller.create_course(request.get_json())

@course_bp.route('/<course_id>', methods=['PUT'])
def update_course(course_id):
    return course_controller.update_course(course_id, request.get_json())

@course_bp.route('/<course_id>', methods=['DELETE'])
def delete_course(course_id):
    return course_controller.delete_course(course_id)
    
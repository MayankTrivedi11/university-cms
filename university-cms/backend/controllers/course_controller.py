from flask import jsonify, request
from services import course_service
from validators import course_validator

def get_all_courses():
    courses = course_service.get_all_courses()
    return jsonify(courses), 200

def get_course(course_id):
    course = course_service.get_course(course_id)
    if course:
        return jsonify(course), 200
    return jsonify({'message': 'Course not found'}), 404

def create_course(data):
    errors = course_validator.validate_course(data)
    if errors:
        return jsonify({'errors': errors}), 400

    new_course = course_service.create_course(data)
    return jsonify(new_course), 201

def update_course(course_id, data):
    errors = course_validator.validate_course(data)
    if errors:
        return jsonify({'errors': errors}), 400

    updated_course = course_service.update_course(course_id, data)
    if updated_course:
        return jsonify(updated_course), 200
    return jsonify({'message': 'Course not found'}), 404

def delete_course(course_id):
    if course_service.delete_course(course_id):
        return jsonify({'message': 'Course deleted'}), 200
    return jsonify({'message': 'Course not found'}), 404
    
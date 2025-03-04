import json
from uuid import uuid4
from config import Config
import threading

ledger_lock = threading.Lock()

def get_all_students():
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r') as f:
            data = json.load(f)
            return data.get('students', [])

def get_student(student_id):
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r') as f:
            data = json.load(f)
            students = data.get('students', [])
            for student in students:
                if student['id'] == student_id:
                    return student
            return None

def create_student(data):
    student_id = str(uuid4())
    new_student = {
        'id': student_id,
        'name': data.get('name'),
        'email': data.get('email'),
        'major': data.get('major')
    }

    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r+') as f:
            data = json.load(f)
            students = data.get('students', [])
            students.append(new_student)
            data['students'] = students
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    return new_student

def update_student(student_id, data):
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r+') as f:
            data = json.load(f)
            students = data.get('students', [])
            for i, student in enumerate(students):
                if student['id'] == student_id:
                    students[i].update(data)
                    data['students'] = students
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                    return students[i]
            return None

def delete_student(student_id):
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r+') as f:
            data = json.load(f)
            students = data.get('students', [])
            original_length = len(students)
            data['students'] = [student for student in students if student['id'] != student_id]
            if len(data['students']) < original_length:
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
                return True
            return False
            
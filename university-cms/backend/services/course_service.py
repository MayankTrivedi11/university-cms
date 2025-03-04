import json
from uuid import uuid4
from config import Config
import threading

# Thread lock for safe ledger access
ledger_lock = threading.Lock()

def get_all_courses():
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r') as f:
            data = json.load(f)
            return data.get('courses', [])

def get_course(course_id):
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r') as f:
            data = json.load(f)
            courses = data.get('courses', [])
            for course in courses:
                if course['id'] == course_id:
                    return course
            return None

def create_course(data):
    course_id = str(uuid4())
    new_course = {
        'id': course_id,
        'name': data.get('name'),
        'description': data.get('description'),
        'credits': data.get('credits')
    }
    
    ## with open(Config.LEDGER_FILE, 'r+') as f:
    ##    data = json.load(f)
    ##    courses = data.get('courses', [])
    ##    courses.append(new_course)
    ##    data['courses'] = courses
    ##    f.seek(0)
    ##    json.dump(data, f, indent=4)
    ##   f.truncate()
    ## return new_course

    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r+') as f:
            data = json.load(f)
            courses = data.get('courses', [])
            courses.append(new_course)
            data['courses'] = courses
            f.seek(0)  # Rewind to the beginning
            json.dump(data, f, indent=4)
            f.truncate() # Remove remaining part
    return new_course

def update_course(course_id, data):
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r+') as f:
            data = json.load(f)
            courses = data.get('courses', [])
            for i, course in enumerate(courses):
                if course['id'] == course_id:
                    courses[i].update(data)
                    data['courses'] = courses
                    f.seek(0)  # Rewind to the beginning
                    json.dump(data, f, indent=4)
                    f.truncate()  # Remove remaining part
                    return courses[i]
            return None

def delete_course(course_id):
    with ledger_lock:
        with open(Config.LEDGER_FILE, 'r+') as f:
            data = json.load(f)
            courses = data.get('courses', [])
            original_length = len(courses)
            data['courses'] = [course for course in courses if course['id'] != course_id]
            if len(data['courses']) < original_length:  # If a course was deleted
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
                return True
            return False
            
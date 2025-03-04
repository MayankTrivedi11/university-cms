import re

def validate_student(data):
    errors = {}
    if not data.get('name'):
        errors['name'] = 'Name is required'
    if not data.get('email'):
        errors['email'] = 'Email is required'
    elif not is_valid_email(data['email']):
        errors['email'] = 'Invalid email format'
    if not data.get('major'):
        errors['major'] = 'Major is required'

    return errors

def is_valid_email(email):
    # Basic email validation regex
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None
    
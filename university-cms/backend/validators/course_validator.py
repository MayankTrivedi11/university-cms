def validate_course(data):
    errors = {}
    if not data.get('name'):
        errors['name'] = 'Name is required'
    if not data.get('description'):
        errors['description'] = 'Description is required'
    if not data.get('credits'):
        errors['credits'] = 'Credits are required'
    try:
        credits = int(data.get('credits', 0))
        if credits <= 0:
            errors['credits'] = 'Credits must be a positive integer'
    except ValueError:
        errors['credits'] = 'Credits must be an integer'

    return errors
    
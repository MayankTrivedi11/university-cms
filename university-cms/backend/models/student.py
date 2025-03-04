class Student:
    def __init__(self, id, name, email, major):
        self.id = id
        self.name = name
        self.email = email
        self.major = major

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'major': self.major
        }
        
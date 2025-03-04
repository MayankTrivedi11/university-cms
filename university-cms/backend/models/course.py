class Course:
    def __init__(self, id, name, description, credits):
        self.id = id
        self.name = name
        self.description = description
        self.credits = credits

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'credits': self.credits
        }
        
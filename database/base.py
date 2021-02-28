class BaseDB:

    def __init__(self):
        self.values = []

    def get_by_id(self, _id):
        for val in self.values:
            if val.id == _id:
                return val

    def insert(self, new_object):
        self.values.append(new_object)

    def update(self, _id, new_object):
        for val in self.values:
            if val.id == _id:
                val = new_object

from utils.utils import unwrap_list


class BaseDB:

    def __init__(self):
        self.values = []

    def get_by_id(self, _id):
        import pdb
        pdb.set_trace()
        for val in self.values:
            if val.id == _id:
                return val
        #results = [val for val in self.values if val.id == _id]
        #return unwrap_list(results)

    def insert(self, new_object):
        self.values.append(new_object)

    def update(self, _id, new_object):
        """Update post return old post"""
        for val in self.values:
            if val.id == _id:
                val = new_object

    def delete(self, _id):
        for index, val in enumerate(enumerate(self.values)):
            if val.id == _id:
                del self.values[index]
                return val

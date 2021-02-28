from database.base import BaseDB
from models.user import User

users = BaseDB()
# Create a god for testing purposes.
users.values.append(User(id=1, username="god", first_name="god", last_name="god"))

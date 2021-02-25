users = []


def get_user(user_id):
    user = [user for user in users if user.id == user_id]
    if user:
        return user[0]
    else:
        return None

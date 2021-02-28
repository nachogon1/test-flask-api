from models.user import User

# from database.user import users


def unwrap_list(my_list):
    if my_list:
        return my_list[0]
    else:
        return None


#
# def create_god():
#     users.values.append(
#         User(
#             id=1,
#             username="god",
#             first_name="god",
#             last_name="god"
#         )
#     )

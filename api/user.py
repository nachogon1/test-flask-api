from flask_pydantic import validate
from database.user import users

from flask import (
    Blueprint, jsonify
)

from models.user import UserModel, User, UserRef

bp = Blueprint('user', __name__, url_prefix='/api')


# TODO: get all posts from user
# TODO: get specific post
# TODO: edit specific post
# TODO: remove post from user
# TODO: add like system

@bp.route('/users', methods=['GET'])
def get_all_users():
    return jsonify([user.dict() for user in users.values])


@bp.route('/user', methods=['GET'])
@validate()
def get_user(query: UserRef):
    return users.get_by_id(query.user_id).dict()  # Mock insert in db.


@bp.route('/user', methods=['POST'])
@validate()
def create_user(body: UserModel):
    """
    swagger_file: create_post.yml
    """
    user = User(**body.dict())
    users.insert(user)  # Mock insert in db.
    return user.dict()


@bp.route('/user', methods=['PUT'])
@validate()
def edit_user(query: UserRef, body: User):
    # TODO: in reality we should connect it to user
    return users.update(query.user_id, body).dict()


@bp.route('/user', methods=['DELETE'])
def delete_user(query: UserRef):
    return users.delete_user(query.user_id)



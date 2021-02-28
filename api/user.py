from flask_pydantic import validate
from database.user import users

from flask import (
    Blueprint, jsonify
)

from models.user import UserModel, User

bp = Blueprint('user', __name__, url_prefix='/api')


@bp.route('/users', methods=['GET'])
def get_all_users():
    return jsonify([user.dict() for user in users.values])


@bp.route('/user', methods=['POST'])
@validate()
def create_user(body: UserModel):
    user = User(**body.dict())
    users.insert(user)  # Mock insert in db.
    return user.dict()




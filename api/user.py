from simpleflake import simpleflake

from database.post import posts
from database.user import users
from models.post import Post

from flask import (
    Blueprint, request
)

from models.user import UserModel

bp = Blueprint('user', __name__, url_prefix='/api')


# TODO: get all posts from user
# TODO: get specific post
# TODO: edit specific post
# TODO: remove post from user
# TODO: add like system


@bp.route('/user', methods=['POST'])
def create_user(user: UserModel):
    """
    swagger_file: create_post.yml
    """
    user_info = user.dict()
    user_info['id'] = simpleflake()
    users.append(user_info)  # Mock insert in db.
    return user_info


@bp.route('/post/<post_id>', methods=['PUT'])
def edit_post(post_id):
    # TODO: find in db
    #  update point
    # db["post"]
    post = Post(**request.get_json(force=True))
    posts.append(post)  # Mock insert in db.
    return post.dict()


@bp.route('/post/<post_id>', methods=['POST'])
def delete_post(post_id: int):
    pass



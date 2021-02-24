from database.post import posts
from models.post import Post

from flask import (
    Blueprint, request
)


bp = Blueprint('auth', __name__, url_prefix='/api')


# TODO: get all posts from user
# TODO: get specific post
# TODO: edit specific post
# TODO: remove post from user
# TODO: add like system

@bp.route('/post', methods=['POST'])
def create_post():
    post = Post(**request.get_json(force=True))
    posts.append(post)  # Mock insert in db.
    return post.dict()

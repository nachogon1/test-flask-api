from flask_pydantic import validate

from database.post import posts, get_post_from_user, get_post
from database.user import get_user
from models.post import Post, PostModel

from flask import (
    Blueprint, request
)


bp = Blueprint('post', __name__, url_prefix='/api')


@bp.route('/post/<post_id>', methods=['GET'])
def get_single_post(post_id: int):
    return get_post(post_id).dict()


@bp.route('/post/<user_id>', methods=['GET'])
def get_posts_from_user(user_id: int):
    user = get_user(user_id)
    return get_post_from_user(user).dict()


@bp.route('/post', methods=['POST'])
@validate()
def create_post(post: PostModel):
    post = Post(**request.get_json(force=True))
    posts.append(post)  # Mock insert in db.
    return post.dict()


from typing import Union

from flask_pydantic import validate

from database.post import posts
from database.user import users
from models.post import Post, PostModel, PostRef, Comment

from flask import (
    Blueprint
)

from models.user import UserRef

bp = Blueprint('post', __name__, url_prefix='/api')


@bp.route('/posts', methods=['GET'])
def get_all_posts():
    """
    Get all posts.

    This option should only be available for admins.
    """
    return {"posts": [post.dict() for post in posts]}


@bp.route('/post', methods=['GET'])
@validate()
def get_post(query: PostRef):
    """Get post from post id."""
    return users.get_by_id(query.user_id).dict()  # Mock insert in db.


@bp.route('/post', methods=['PUT'])
@validate()
def edit_post(query: UserRef, body: Post):
    # TODO: in reality we should connect it to user
    # update_post(body.id, body.post)
    posts.append(body)  # Mock insert in db.
    return body.dict()


@bp.route('/post', methods=['PUT'])
@validate()
def give_like(query: UserRef, body: Post):
    # TODO: in reality we should connect it to user
    # update_post(body.id, body.post)
    try:
        body.likes.remove(query.user_id)
    except ValueError:
        body.likes.append(query.user_id)

    posts.update(body.id, body)  # Mock insert in db.
    return body.dict()


@bp.route('/post/comment', methods=['POST'])
@validate()
def make_comment(query: Union[UserRef, PostRef], body: Comment):
    post = posts.get_by_id(query.post_id)
    body.author = query.user_id
    post.comments.append(body)
    posts.update(post.id, post)  # Mock insert in db.
    return body.dict()


@bp.route('/post', methods=['POST'])
@validate()
def create_post(query: UserRef, body: PostModel):
    # TODO: in reality we should connect it to user
    post = Post(**body.dict())
    user = users.get_by_id(query.user_id)
    user.post_ids.append(post)
    users.update(query.user_id, user)
    posts.insert(post)  # Mock insert in db.
    return post.dict()

# TODO comment on why 2 collections. Make comment as colection?


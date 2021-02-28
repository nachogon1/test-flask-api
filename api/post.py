from flask_pydantic import validate

from database.post import posts
from database.user import users
from models.post import Post, PostModel, Comment, UserPostRef

from flask import Blueprint, jsonify

from models.user import UserRef

bp = Blueprint("post", __name__, url_prefix="/api")


@bp.route("/posts", methods=["GET"])
def get_all_posts():
    return jsonify([post.dict() for post in posts.values])


@bp.route("/post/like", methods=["PUT"])
@validate()
def give_like(query: UserPostRef):
    post = posts.get_by_id(query.post_id)
    try:
        post.likes.remove(query.user_id)
    except ValueError:
        post.likes.append(query.user_id)

    posts.update(post.id, post)  # Mock insert in db.
    return post.dict()


@bp.route("/post/comment", methods=["POST"])
@validate()
def make_comment(query: UserPostRef, body: Comment):
    post = posts.get_by_id(query.post_id)
    body.author_id = query.user_id
    post.comments.append(body)
    posts.update(post.id, post)  # Mock insert in db.
    return body.dict()


@bp.route("/post", methods=["POST"])
@validate()
def create_post(query: UserRef, body: PostModel):
    post = Post(**body.dict())
    user = users.get_by_id(query.user_id)
    user.post_ids.append(post)
    users.update(query.user_id, user)
    posts.insert(post)  # Mock insert in db.
    return post.dict()


# TODO comment on why 2 collections. Make comment as colection?

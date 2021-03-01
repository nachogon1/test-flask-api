from database.post import posts
from database.user import users

KEYS = ["id", "created", "changed"]


def test_post(test_client):

    # Create a user to add a post to
    response = test_client.post(
        "/api/user",
        json={
            "username": "test_username",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
        },
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    result = response.json
    user_id = result["id"]
    # Check how many posts has done the user.
    test_user = users.get_by_id(user_id)
    assert len(test_user.post_ids) == 0

    # Create post to user
    response = test_client.post(
        f"/api/post?user_id={user_id}",
        json={"title": "test_title", "description": "test_description"},
    )
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    result = response.json
    assert all([key in result for key in KEYS])
    post_id = result["id"]
    # Check how many posts has done the user.
    test_user = users.get_by_id(user_id)
    assert len(test_user.post_ids) == 1
    # Check that it is the created post.
    assert test_user.post_ids[0] == post_id
    # Check that the post has no likes.
    assert len(posts.get_by_id(post_id).likes) == 0

    # Like a post
    response = test_client.put(f"/api/post/like?user_id={user_id}&post_id={post_id}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    result = response.json
    assert all([key in result for key in KEYS])
    # Check that the post has one like.
    assert len(posts.get_by_id(post_id).likes) == 1

    # Dislike a post
    response = test_client.put(f"/api/post/like?user_id={user_id}&post_id={post_id}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    result = response.json
    assert all([key in result for key in KEYS])
    # Check that the post has one like.
    assert len(posts.get_by_id(post_id).likes) == 0

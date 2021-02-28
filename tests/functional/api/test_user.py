from database.user import users

KEYS = ["id", "created", "changed"]


def test_user(test_client):

    # Test create user
    response = test_client.post("/api/user",
                                json={"username": "test_username",
                                      "first_name": "test_first_name",
                                      "last_name": "test_last_name"})

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    result = response.json
    assert result["first_name"] == "test_first_name"
    assert all([key in result for key in KEYS])
    assert len(users.values) == 1

    # Test get all users
    response = test_client.get("/api/users")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    result = response.json
    assert type(result) == list
    assert len(result) == 1





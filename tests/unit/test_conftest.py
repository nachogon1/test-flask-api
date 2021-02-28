import mock


@mock.patch("tests.conftest.posts")
@mock.patch("tests.conftest.users")
def test_teardown_db(posts, users):
    from tests.conftest import teardown_db

    posts.values = ["foobar"]
    users.values = ["barfoo"]
    teardown_db()
    assert posts.values == []
    assert users.values == []

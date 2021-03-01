from pytest import fixture

from database.post import posts
from database.user import users
from main import create_app


@fixture
def app():

    # We are not messing with env variables in this api.
    # We have a mock db, thus we won't configure a testing db.
    app = create_app()

    yield app


def teardown_db():
    
    posts.values = []
    users.values = []


@fixture
def test_client(app):
    teardown_db()
    yield app.test_client()

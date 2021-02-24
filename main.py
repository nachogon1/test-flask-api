from flask import Flask, url_for, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators

from api import user
from models.user import User


def create_app():
    _app = Flask(__name__)
    _app.register_blueprint(user.bp)

    return _app


app = create_app()


@app.route('/')
def hello_world():
    return 'Hello, World!'
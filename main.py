import os

from flask import Flask, url_for, request
from flask_swagger import swagger
from wtforms import Form, BooleanField, StringField, PasswordField, validators

from api import user
from models.user import User

from flask import current_app
from json import dumps


def jsonify(*args, **kwargs):
    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1:  # single args are passed directly to dumps()
        data = args[0]
    else:
        data = args or kwargs

    return current_app.response_class(
        dumps(data) + '\n',
        mimetype=current_app.config['JSONIFY_MIMETYPE']
    )


def create_app():
    _app = Flask(__name__)
    _app.register_blueprint(user.bp)

    return _app


app = create_app()
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route("/spec")
def spec():
    swag = swagger(app)
    base_path = os.path.join(app.root_path, 'swagger_files')
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Test-Flask-API"
    return jsonify(swag, from_file_keyword="swagger_file", base_path=base_path)


@app.route('/')
def hello_world():
    return 'Hello, World!'
from flask import Flask

from api import user, post
from swagger_files.config import api as _api

try:
    from flask_restplus import Resource, Api, fields
except ImportError:
    import werkzeug

    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource, Api, fields


def create_app():
    _app = Flask(__name__)
    _app.register_blueprint(user.bp)
    _app.register_blueprint(post.bp)

    return _app


app = create_app()
_api.init_app(app=app)

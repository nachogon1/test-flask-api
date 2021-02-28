import os

from flask import Flask
from flask_swagger import swagger

from api import user, post

from flask import current_app
from json import dumps

from api.user import get_all_users
from database.user import users

try:
    from flask_restplus import Resource, Api, fields
except ImportError:
    import werkzeug

    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource, Api, fields


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
    api = Api(app=_app)
    api.init_app(user.bp)
    ns = api.namespace('', description="Endpoints.")
    _app.register_blueprint(user.bp)
    _app.register_blueprint(post.bp)
    # _app.init_app(user.bp)

    return _app, ns, api


app, ns, api = create_app()

user_model = api.model('UserModel',
                       {'id': fields.Integer(readonly=True, description='Main key'),
                        'username': fields.String(required=True),
                        'first_name': fields.String(required=True),
                        'last_name': fields.String(required=False),
                        'changed': fields.String(required=False),
                        'created': fields.String(required=False)
                        }
                       )

create_user_model = api.model(
    'CreateUserModel',
    {
        'username': fields.String(required=True),
        'first_name': fields.String(required=True),
        'last_name': fields.String(required=False),
    }
)


@ns.route('/users')
class UsersSwagger(Resource):
    """Apis related to users"""

    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        pass


from flask_restplus import reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, location='body')


@ns.route('/user')
@api.header('Content-Type', 'application/json')
class UserSwagger(Resource):
    """Api related to single users"""

    @ns.doc('create_user')
    @ns.expect(create_user_model)
    @ns.marshal_list_with(user_model)
    @ns.marshal_with(user_model)
    def post(self):
        """Create a user"""
        pass

# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# @app.route("/spec")
# def spec():
#     swag = swagger(app)
#     #base_path = os.path.join(app.root_path, 'swagger_files')
#     swag['info']['version'] = "1.0"
#     swag['info']['title'] = "Test-Flask-API"
#     return jsonify(swag)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

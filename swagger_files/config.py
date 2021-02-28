try:
    from flask_restplus import Resource, fields, Api, Namespace
except ImportError:
    import werkzeug

    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Resource, fields, Api, Namespace


ns = Namespace('api', description='Send requests to the API endpoints.')
api = Api(title="Test Flask API  Swagger")
api.add_namespace(ns)

user_model = api.model('UserModel',
                       {'id': fields.String(readonly=True, description='Main key'),
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



create_post_model = api.model(
    'CreatePostModel',
    {
        'title': fields.String(required=True),
        'description': fields.String(required=False)
    }
)

create_comment = api.model(
    'CreateCommentModel',
    {
        'text': fields.String(required=True),
        'author_id': fields.String(required=True)
    }
)


@ns.route('/users')
class UsersSwagger(Resource):

    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        pass


@ns.route('/user')
@api.header('Content-Type', 'application/json')
class UserSwagger(Resource):

    @ns.doc('create_user')
    @ns.expect(create_user_model)
    @ns.marshal_list_with(user_model)
    @ns.marshal_with(user_model)
    def post(self):
        """Create a user"""
        pass


@ns.route('/post?user_id=<int:user_id>')
@api.header('Content-Type', 'application/json')
class PostSwagger(Resource):

    @ns.doc('create_post')
    @ns.expect(create_post_model)
    def post(self):
        """Create a post"""
        pass


@ns.route('/post/comment?user_id=<int:user_id>&post_id=<int:post_id>')
@api.header('Content-Type', 'application/json')
class MakeComment(Resource):

    @ns.doc('make a comment')
    @ns.expect(create_comment)
    def post(self):
        """Make a comment to a post"""
        pass


@ns.route('/posts')
class PostsSwagger(Resource):

    @ns.doc('list_posts')
    def get(self):
        """List all posts"""
        pass


@ns.route('/post/like?user_id=<int:user_id>&post_id=<int:post_id>')
@api.header('Content-Type', 'application/json')
class GiveLike(Resource):

    @ns.doc('give_a_like')
    def put(self):
        """Give a like to a post"""
        pass
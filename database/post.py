from utils.utils import unwrap_list

posts = []


def get_post(post_id):
    post = [post for post in posts if post.id == post_id]
    return unwrap_list(post)


def get_post_from_user(user):
    post = [post for post in posts if post.id in user.comments]
    return unwrap_list(post)

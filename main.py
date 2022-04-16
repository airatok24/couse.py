from flask import Blueprint, render_template, request
from utils import get_post_by_id, load_candidates_from_json, load_comments_from_json, get_comments_by_post_id, search_for_posts, get_posts_by_user

main_blueprint = Blueprint('main', __name__, template_folder='templates')

data = load_candidates_from_json()
comments = load_comments_from_json()


@main_blueprint.route('/')
def main():
    posts = data
    return render_template("index.html", posts=posts)


@main_blueprint.route('/posts/<int:pk>')
def post(pk):
    post = get_post_by_id(pk)
    comments = get_comments_by_post_id(pk)
    pk = pk
    return render_template("post.html", post=post, comments=comments, pk=pk)


@main_blueprint.route('/search/')
def search():
    search_by = request.args['s']
    posts: list[dict] = search_for_posts(search_by)
    return render_template("search.html", search_by=search_by, posts=posts)


@main_blueprint.route('/users/<username>')
def search_user_posts(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', username=username, posts=posts)

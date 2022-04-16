from flask import Blueprint, render_template, request, jsonify
from utils import load_candidates_from_json,get_post_by_id


api_blueprint = Blueprint('api', __name__, template_folder='templates')


@api_blueprint.route('/api/posts')
def api_get_post():
    posts = load_candidates_from_json()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<post_id>')
def api_post(post_id):
    post = get_post_by_id(int(post_id))
    return jsonify(post)




import json

POST_PATH = "data.json"
COMMENTS = "comments.json"

__comments = []
__data = []


def load_candidates_from_json():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_comments_from_json():
    with open(COMMENTS, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_post_by_id(pk):
    for post in load_candidates_from_json():
        if post['pk'] == pk:
            return post


def get_comments_by_post_id(pk):
    post_id_comments = []
    for comment in load_comments_from_json():
        if comment['post_id'] == pk:
            post_id_comments.append(comment)
    return post_id_comments


def search_for_posts(query: str) -> list[dict]:
    return [post for post in load_candidates_from_json() if query.lower() in post['content'].lower()]


def get_posts_by_user(username):
    users_posts = []
    for post in load_candidates_from_json():
        if username.lower() in post['poster_name'].lower():
            users_posts.append(post)
    return users_posts

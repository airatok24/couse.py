import pytest
from app import app


def test_get_posts_all():
    response = app.test_client().get('api/posts/1')
    assert response.status_code == 200
    assert set(response.json.keys()) == {
        'content', 'pic', 'likes_count', 'pk', 'poster_name', 'poster_avatar', 'views_count'
    }


def test_get_post():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0

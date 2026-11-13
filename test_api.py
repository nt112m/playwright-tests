import requests


def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_post_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
    assert response.status_code == 404
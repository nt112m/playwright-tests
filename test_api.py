import requests


def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_post_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
    assert response.status_code == 404

def test_get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100

def test_create_post():
    new_post = {"title": "hello", "body": "my first post", "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
    assert response.status_code == 201
    assert response.json()["title"] == "hello"

# -*- coding: UTF-8 -*-
from main.mongodb_dm import Blog

base_api_path = '/xcms/api/blogs'


def test_get_blogs(client, app):
    assert client.get(base_api_path).status_code == 200
    with app.app_context():
        assert app.db[Blog.tablename].count_documents({}) == 2


def test_get_blog(client, app):
    assert client.get(base_api_path + '/1').status_code == 200
    with app.app_context():
        assert app.db[Blog.tablename].count_documents({}) == 2

    assert client.get(base_api_path + '/3').status_code == 404


def test_post_blog(client, auth, app):
    assert client.post(base_api_path).status_code == 401

    assert client.post(base_api_path, headers=auth).status_code == 400
    assert client.post(base_api_path, headers=auth, json={"test": "test"}).status_code == 400

    resp = client.post(base_api_path, headers=auth,
                       json={"title": "Post Testing Title",
                             "author": "Post Testing Author",
                             "tags": ["post_tag1", "post_tag2"],
                             "content": "I am post testing data, I am post testing data."})
    assert resp.status_code == 201
    with app.app_context():
        assert app.db[Blog.tablename].count_documents({}) == 3

    resp = client.post(base_api_path, headers=auth,
                       json={"title": "Post Testing Title",
                             "author": "Post Testing Author",
                             "tags": ["post_tag1", "post_tag2"],
                             "content": "I am post testing data, I am post testing data."})
    assert resp.status_code == 409
    with app.app_context():
        assert app.db[Blog.tablename].count_documents({}) == 3


def test_put_blog(client, auth, app):
    assert client.put(base_api_path + '/1').status_code == 401

    assert client.put(base_api_path + '/1', headers=auth).status_code == 400
    assert client.put(base_api_path + '/1', headers=auth, json={"test": "test"}).status_code == 400

    resp1 = client.put(base_api_path + '/1', headers=auth,
                       json={"title": "Updated Testing Title",
                             "author": "Testing Author",
                             "tags": ["tag1", "tag2"],
                             "content": "I am testing data, I am testing data."})
    assert resp1.status_code == 201
    with app.app_context():
        doc = app.db[Blog.tablename].find_one({'_id': 1})
        assert doc['title'] == 'Updated Testing Title'

    resp2 = client.put(base_api_path + '/3', headers=auth,
                       json={"title": "Updated Testing Title",
                             "author": "Testing Author",
                             "tags": ["tag1", "tag2"],
                             "content": "I am testing data, I am testing data."})
    assert resp2.status_code == 404


def test_delete_blog(client, auth, app):
    assert client.delete(base_api_path + '/1').status_code == 401

    assert client.delete(base_api_path + '/1', headers=auth).status_code == 201
    with app.app_context():
        doc = app.db[Blog.tablename].find_one({'_id': 1})
        assert doc is None

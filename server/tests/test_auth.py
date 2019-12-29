# -*- coding: UTF-8 -*-
import json


def test_register(client):
    URI = '/xcms/auth/api/v1.0/register'
    # 没有request.json
    assert client.post(URI).status_code == 400
    # request.json中有password，没有username
    assert client.post(URI, json={'password': 'test'}).status_code == 400
    # request.json中有username，没有password
    assert client.post(URI, json={'username': 'test'}).status_code == 400
    # 注册成功
    assert client.post(URI, json={'username': 'test', 'password': 'test'}).status_code == 201
    # 用户已存在
    resp = client.post(URI, json={'username': 'test', 'password': 'test'})
    assert resp.status_code == 400
    assert json.loads(resp.data).get('msg') == 'User <test> is existed'


def test_login(auth, client):
    URI = '/xcms/auth/api/v1.0/login'
    # 没有request.json
    assert client.post(URI).status_code == 400
    # request.json中有password，没有username
    assert client.post(URI, json={'password': 'test'}).status_code == 400
    # request.json中有username，没有password
    assert client.post(URI, json={'username': 'test'}).status_code == 400
    # 用户不存在
    assert client.post(URI, json={'username': 'test1', 'password': ''}).status_code == 404
    # 登陆成功
    resp = client.post(URI, json={'username': 'test', 'password': 'test'})
    assert json.loads(resp.data).get('token') is not None

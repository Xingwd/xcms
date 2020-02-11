# -*- coding: UTF-8 -*-
import json


URL_PREFIX = '/api/auth'


def test_register(client):
    URI = URL_PREFIX + '/v1.0/register'
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
    URI = URL_PREFIX + '/v1.0/login'
    # 没有request.json
    assert client.post(URI).status_code == 400
    # request.json中有password，没有username
    assert client.post(URI, json={'password': 'test'}).status_code == 400
    # request.json中有username，没有password
    assert client.post(URI, json={'username': 'test'}).status_code == 400
    # 用户不存在
    assert client.post(URI, json={'username': 'test1', 'password': ''}).status_code == 404
    # 密码错误
    assert client.post(URI, json={'username': 'test', 'password': ''}).status_code == 400
    # 登陆成功
    resp = client.post(URI, json={'username': 'test', 'password': 'test'})
    assert json.loads(resp.data).get('token') is not None


def test_verify_token(auth, client):
    URI = URL_PREFIX + '/v1.0/verify_token'
    # 没有request.json
    assert client.post(URI).status_code == 400
    # 无效的token
    resp1 = client.post(URI, json={'token': ''})
    assert resp1.status_code == 401
    assert json.loads(resp1.data) is False
    # 有效的token
    login_resp = client.post(URL_PREFIX + '/v1.0/login', json={'username': 'test', 'password': 'test'})
    token = json.loads(login_resp.data).get('token')
    resp2 = client.post(URI, json={'token': token})
    assert resp2.status_code == 200
    assert json.loads(resp2.data) is True

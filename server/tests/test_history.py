# -*- coding: UTF-8 -*-
import pytest
import json
from main import db
from main.models import History


URL_PREFIX = '/api/history/v1.0/histories'


@pytest.fixture()
def init(app):
    with app.app_context():
        history = History(time='2020.02', release='v1.0.0', description='测试')
        db.session.add(history)
        db.session.commit()


def test_get_histories(init, client):
    # 全部数据
    resp1 = client.get(URL_PREFIX)
    assert resp1.status_code == 200
    assert len(json.loads(resp1.data)) == 1
    assert json.loads(resp1.data)[0].get('time') == '2020.02'


def test_create_history(init, auth, client):
    # 认证失败
    assert client.post(URL_PREFIX).status_code == 401
    # 没有request.json
    assert client.post(URL_PREFIX, headers=auth).status_code == 400
    # request.json中没有time
    assert client.post(URL_PREFIX, headers=auth, json={'release': 'v1.0.1', 'description': '测试'}).status_code == 400
    # request.json中没有release
    assert client.post(URL_PREFIX, headers=auth, json={'time': '2020.03', 'description': '测试'}).status_code == 400
    # request.json中没有description
    assert client.post(URL_PREFIX, headers=auth, json={'time': '2020.03', 'release': 'v1.0.1'}).status_code == 400
    # 成功创建
    data = {
        'time': '2020.03',
        'release': 'v1.0.1',
        'description': '测试'
    }
    assert client.post(URL_PREFIX, headers=auth, json=data).status_code == 201
    # 验证创建
    assert json.loads(client.get(URL_PREFIX).data)[0].get('time') == '2020.03'


def test_update_history(init, auth, client):
    # 认证失败
    assert client.put(URL_PREFIX + '/1').status_code == 401
    # 没有request.json
    assert client.put(URL_PREFIX + '/1', headers=auth).status_code == 400
    # request.json中没有time
    assert client.put(URL_PREFIX + '/1', headers=auth, json={'release': 'v1.0.1', 'description': '测试'}).status_code == 400
    # request.json中没有release
    assert client.put(URL_PREFIX + '/1', headers=auth, json={'time': '2020.03', 'description': '测试'}).status_code == 400
    # request.json中没有description
    assert client.put(URL_PREFIX + '/1', headers=auth, json={'time': '2020.03', 'release': 'v1.0.1'}).status_code == 400
    # 没有找到
    assert client.put(
        URL_PREFIX + '/10',
        headers=auth,
        json={
            'time': '2020.03',
            'release': 'v1.0.1',
            'description': '测试'
        }
    ).status_code == 404
    # 成功更新
    data = {
        'time': '2020.03',
        'release': 'v1.0.1',
        'description': '测试'
    }
    assert client.put(URL_PREFIX + '/1', headers=auth, json=data).status_code == 201
    # 验证更新
    assert json.loads(client.get(URL_PREFIX).data)[0].get('time') == '2020.03'


def test_delete_history(init, auth, client):
    # 认证失败
    assert client.delete(URL_PREFIX + '/1').status_code == 401
    # 没有找到
    assert client.delete(URL_PREFIX + '/10', headers=auth).status_code == 404
    # 删除成功
    assert client.delete(URL_PREFIX + '/1', headers=auth).status_code == 201
    # 验证删除
    assert len(json.loads(client.get(URL_PREFIX).data)) == 0

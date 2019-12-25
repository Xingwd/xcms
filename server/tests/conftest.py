# -*- coding: UTF-8 -*-
"""
测试
"""
import pytest
import base64
from main import create_app
from conf.config import TestingConfig
from main.mongodb_dm import User, Blog

# TODO: 调整测试逻辑
test_user = {'username': 'test', 'password': 'test'}

test_blogs = [
                {"title": "Testing Title1", "author": "Testing Author1", "tags": ["tag1", "tag2"], "content": "I am testing data, I am testing data."},
                {"title": "Testing Title2", "author": "Testing Author2", "tags": ["tag3", "tag4"], "content": "I am testing data, I am testing data."}
            ]


@pytest.fixture
def app():
    app = create_app(config=TestingConfig)

    # User 测试数据
    User(app=app).insert_one(test_user['username'], test_user['password'])
    # Blog 测试数据
    blog = Blog(app=app)
    for tb in test_blogs:
        blog.insert_one(tb['title'], tb['author'], tb['tags'], tb['content'])

    # Other 测试数据

    yield app

    # 清理数据
    app.db.command("dropDatabase")


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth(app):
    b64_user = str(base64.b64encode('{}:{}'.format(test_user['username'], test_user['password']).encode('utf-8')), 'utf-8')
    return {'Authorization': 'Basic ' + b64_user}

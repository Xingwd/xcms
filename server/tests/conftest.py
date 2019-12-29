# -*- coding: UTF-8 -*-
"""
测试
"""
import os
import tempfile
import pytest
# import base64
from main import create_app, db
from config import TestingConfig

# # TODO: 调整测试逻辑
# test_user = {'username': 'test', 'password': 'test'}
#


@pytest.fixture()
def app():
    db_fd, db_file = tempfile.mkstemp()
    TestingConfig.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file
    app = create_app(config=TestingConfig)

    with app.app_context():
        db.create_all()
    yield app

    os.close(db_fd)
    os.unlink(db_file)


@pytest.fixture()
def client(app):
    with app.test_client() as client:
        yield client

#
# @pytest.fixture
# def auth(app):
#     b64_user = str(base64.b64encode('{}:{}'.format(test_user['username'], test_user['password']).encode('utf-8')), 'utf-8')
#     return {'Authorization': 'Basic ' + b64_user}

# -*- coding: UTF-8 -*-
"""
测试
"""
import os
import tempfile
import pytest
import base64
from config import TestingConfig
from main import create_app, db
from main.models import User


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


@pytest.fixture()
def auth(app):
    token = None
    with app.app_context():
        user = User(username='test')
        user.hash_password('test')
        db.session.add(user)
        db.session.commit()
        token = User.query.filter_by(username='test').first().generate_token().decode('ascii')
    basic = str(base64.b64encode('{}:{}'.format(token, 'unused').encode('utf-8')), 'utf-8')
    return {'Authorization': 'Basic {}'.format(basic)}

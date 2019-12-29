# -*- coding: UTF-8 -*-
"""
测试
"""
import os
import tempfile
import pytest
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
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
    with app.app_context():
        user = User(username='test')
        user.hash_password('test')
        db.session.add(user)
        db.session.commit()
    # s = Serializer(app.config['SECRET_KEY'])
    # return {'Authorization': 'Token ' + s.dumps({'id': 1})}

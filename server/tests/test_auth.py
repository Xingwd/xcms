# -*- coding: UTF-8 -*-
from server.main.mongodb_dm import User

base_api_path = '/xcms/api/auth'


def test_register(client, app):
    assert client.post(base_api_path + '/register').status_code == 400
    assert client.post(base_api_path + '/register', json={"test": "test"}).status_code == 400

    resp1 = client.post(base_api_path + '/register', json={"username": "test_register", "password": "test_register"})
    assert resp1.status_code == 201
    with app.app_context():
        assert app.db[User.tablename].count_documents({}) == 2

    resp2 = client.post(base_api_path + '/register', json={"username": "test_register", "password": "test_register"})
    assert resp2.status_code == 409
    with app.app_context():
        assert app.db[User.tablename].count_documents({}) == 2

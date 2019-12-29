from main import create_app


# TODO: 调整测试逻辑
def test_config(app):
    assert not create_app().testing
    assert app.testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'

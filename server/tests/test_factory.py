from main import create_app
from conf.config import TestingConfig


# TODO: 调整测试逻辑
def test_config():
    assert not create_app().testing
    assert create_app(config=TestingConfig).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'

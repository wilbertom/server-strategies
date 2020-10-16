import pytest
import requests

@pytest.fixture
def config():
    return {
        'server': 'http://localhost:1337',
    }


def test_getting_hello_world_message(config):
    response = requests.get(config['server'])

    assert response.status_code == 200
    assert response.content.decode('utf8') == 'hello, world'

import pytest
import requests
from requests_futures.sessions import FuturesSession
from concurrent.futures import ThreadPoolExecutor


@pytest.fixture
def config():
    return {
        'server': 'http://localhost:1337',
        'async-pool-size': None,
    }


def assertResponses(config, n):
    for _ in range(0, n):
        response = requests.get(config['server'])

        assert response.status_code == 200
        assert response.content.decode('utf8') == 'hello, world'


def assertResponsesAsync(config, n):
    pool_size = config['async-pool-size']
    executor = None if pool_size is None else ThreadPoolExecutor(max_workers=pool_size)
    session = FuturesSession(executor=executor)
    futures = [session.get(config['server']) for _ in range(0, n)]

    for f in futures:
        response = f.result()
        assert response.status_code == 200
        assert response.content.decode('utf8') == 'hello, world'


def test_getting_hello_world_message_1_times(config):
    assertResponses(config, 1)

def test_getting_hello_world_message_10_times(config):
    assertResponses(config, 10)

def test_getting_hello_world_message_100_times(config):
    assertResponses(config, 100)

def test_getting_hello_world_message_1000_times(config):
    assertResponses(config, 1000)

# asynchronous requests

def test_getting_hello_world_message_1_times_async(config):
    assertResponsesAsync(config, 1)

def test_getting_hello_world_message_10_times_async(config):
    assertResponsesAsync(config, 10)

def test_getting_hello_world_message_100_times_async(config):
    assertResponsesAsync(config, 100)

def test_getting_hello_world_message_1000_times_async(config):
    assertResponsesAsync(config, 1000)

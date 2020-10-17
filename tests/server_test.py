import pytest
import requests
from requests_futures.sessions import FuturesSession
from concurrent.futures import ThreadPoolExecutor
import os


@pytest.fixture
def config():
    return {
        'server': f'http://localhost:{os.environ["PORT"]}',
        'async-pool-size': int(os.environ.get("POOL_SIZE", '0')),
        'requests': int(os.environ['REQUESTS']),
        'mode': os.environ['MODE'],
    }

def test_getting_hello_world(config):
    if config['mode'] == 'sync':
        for _ in range(config['requests']):
            response = requests.get(config['server'])

            assert response.status_code == 200
            assert response.content.decode('utf8') == 'hello, world'
    else:
        pool_size = config['async-pool-size']
        executor = ThreadPoolExecutor(max_workers=pool_size)
        session = FuturesSession(executor=executor)
        futures = [session.get(config['server']) for _ in range(config['requests'])]

        for f in futures:
            response = f.result()
            assert response.status_code == 200
            assert response.content.decode('utf8') == 'hello, world'

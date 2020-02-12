from unittest import mock

import redis
import pytest

from config import REDIS_DSN, STORAGE_NAME
from main import create_app


@pytest.fixture
def initial_rates():
    return [
        {'currency': 'USD', 'rate': 63.379},
        {'currency': 'EUR', 'rate': 69.182},
    ]


@pytest.fixture
def cli(loop, aiohttp_client):
    app = create_app()
    return loop.run_until_complete(aiohttp_client(app))


@pytest.fixture()
def redis_cli():
    conn = redis.from_url(REDIS_DSN)
    yield conn
    conn.close()


@pytest.fixture(autouse=True)
def prepare_rates(redis_cli, initial_rates):
    redis_cli.delete(STORAGE_NAME)
    for rate in initial_rates:
        redis_cli.hset(STORAGE_NAME, rate['currency'], rate['rate'])


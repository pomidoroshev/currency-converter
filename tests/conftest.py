from unittest import mock

import pytest

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


@pytest.fixture(autouse=True)
def prepare_rates(cli, loop, initial_rates):
    loop.run_until_complete(cli.post('/database', json=initial_rates))
    yield
    loop.run_until_complete(cli.post('/database', json=[]))

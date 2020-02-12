from config import STORAGE_NAME

import pytest


async def test_database_rewrite(cli, redis_cli):
    resp = await cli.post('/database', json=[{'currency': 'EUR', 'rate': 78}])
    assert resp.status == 200
    assert not redis_cli.hget(STORAGE_NAME, 'USD')
    assert redis_cli.hget(STORAGE_NAME, 'EUR') == b'78'


async def test_database_clear(cli, redis_cli):
    resp = await cli.post('/database', json=[])
    assert resp.status == 200
    assert not redis_cli.hget(STORAGE_NAME, 'USD')
    assert not redis_cli.hget(STORAGE_NAME, 'EUR')


async def test_database_merge(cli, redis_cli):
    resp = await cli.post(
        '/database', params={'merge': 1}, json=[{'currency': 'EUR', 'rate': 78}]
    )
    assert resp.status == 200
    assert redis_cli.hget(STORAGE_NAME, 'EUR') == b'78'
    assert redis_cli.hget(STORAGE_NAME, 'USD')


@pytest.mark.parametrize('rates', [
    [{'foo': 'bar'}],
    [{'currency': 123, 'rate': 'RUR'}],
])
async def test_database_bad_request(cli, rates):
    resp = await cli.post('/database', json=rates)
    assert resp.status == 400

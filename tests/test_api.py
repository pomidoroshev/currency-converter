import pytest

from config import STORAGE_NAME


@pytest.fixture(autouse=True)
async def prepare_rates(redis):
    await redis.hset(STORAGE_NAME, 'USD', '63.379')
    await redis.hset(STORAGE_NAME, 'EUR', '69.182')


@pytest.mark.parametrize(['params', 'expected'], [
    ({'from': 'RUR', 'to': 'USD', 'amount': 42}, {'currency': 'USD', 'amount': 0.66}),
    ({'from': 'USD', 'to': 'EUR', 'amount': 10}, {'currency': 'EUR', 'amount': 9.16}),
])
async def test_convert(cli, params, expected):
    resp = await cli.get('/convert', params=params)
    assert resp.status == 200
    assert await resp.json() == expected


@pytest.mark.parametrize('params', [
    {'from': 'RUR', 'amount': 42},
    {'from': 'RUR', 'amount': 'foo'},
    {},
])
async def test_convert_bad_request(cli, params):
    resp = await cli.get('/convert', params=params)
    assert resp.status == 400


async def test_database(cli):
    resp = await cli.post('/database')
    assert resp.status == 200

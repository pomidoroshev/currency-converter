import pytest

from config import STORAGE_NAME


@pytest.mark.parametrize(['params', 'expected'], [
    ({'from': 'RUR', 'to': 'USD', 'amount': 42}, {'currency': 'USD', 'amount': 0.66}),
    ({'from': 'USD', 'to': 'EUR', 'amount': 10}, {'currency': 'EUR', 'amount': 9.16}),
])
async def test_convert(params, expected, cli):
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


@pytest.mark.parametrize('params', [
    {'from': 'FOO', 'to': 'USD', 'amount': 42},
    {'from': 'RUR', 'to': 'BAR', 'amount': 42},
])
async def test_convert_not_found(cli, params):
    resp = await cli.get('/convert', params=params)
    assert resp.status == 404

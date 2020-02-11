import pytest


async def test_database_update(cli):
    resp = await cli.post('/database', json=[
        {'currency': 'EUR', 'rate': 69.182},
    ])
    assert resp.status == 200

    resp = await cli.get('/convert', params={
        'from': 'EUR',
        'to': 'USD',
        'amount': 1
    })
    assert resp.status == 404


async def test_database_merge(cli):
    resp = await cli.post('/database', params={'merge': 1}, json=[
        {'currency': 'EUR', 'rate': 69.182},
    ])
    assert resp.status == 200

    resp = await cli.get('/convert', params={
        'from': 'EUR',
        'to': 'USD',
        'amount': 1
    })
    assert resp.status == 200


@pytest.mark.parametrize('rates', [
    [{'foo': 'bar'}],
    [{'currency': 123, 'rate': 'RUR'}],
])
async def test_database_bad_request(cli, rates):
    resp = await cli.post('/database', json=rates)
    assert resp.status == 400

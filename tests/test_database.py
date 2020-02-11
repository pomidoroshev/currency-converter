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

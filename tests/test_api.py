async def test_convert(cli):
    resp = await cli.get('/convert')
    assert resp.status == 200


async def test_database(cli):
    resp = await cli.post('/database')
    assert resp.status == 200

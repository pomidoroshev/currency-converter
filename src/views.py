from aiohttp import web
import ujson

from errors import UnknownCurrencyError
from money import Money
from schemas import *

__all__ = ('convert', 'database')


DEFAULT_CURRENCY = 'RUR'


async def convert(request):
    try:
        params = ConvertRequestSchema().load(request.query)
        result = await request.app['converter'].convert(
            Money(params['amount'], params['from']), params['to']
        )
    except ValidationError as e:
        return json_response({'error': e.messages}, status=400)
    except UnknownCurrencyError as e:
        return json_response({'error': str(e)}, status=404)

    return json_response(result.to_json())


async def database(request):
    try:
        rates = RateSchema(many=True).load(await request.json())
    except ValidationError as e:
        return json_response({'error': e.messages}, status=400)

    merge = bool(int(request.query.get('merge', 0)))
    await request.app['converter'].update(rates, merge)
    return web.Response()


def json_response(*args, **kwargs):
    return web.json_response(*args, **kwargs, dumps=ujson.dumps)

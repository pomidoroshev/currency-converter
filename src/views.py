from aiohttp import web
import ujson

from money import Money
from schemas import *

__all__ = ('convert', 'database')


DEFAULT_CURRENCY = 'RUR'


async def convert(request):
    try:
        params = ConvertRequestSchema().load(request.query)
    except ValidationError as e:
        return json_response(e.messages, status=400)

    result = await request.app['converter'].convert(
        Money(params['amount'], params['from']), params['to']
    )

    return json_response(result.to_json())


async def database(request):
    return web.Response()


def json_response(*args, **kwargs):
    return web.json_response(*args, **kwargs, dumps=ujson.dumps)

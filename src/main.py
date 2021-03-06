from aiohttp import web
import aioredis
import uvloop

from config import REDIS_DSN, STORAGE_NAME
from converter import Converter
from storage import Storage
from views import *


async def start_redis(app):
    redis = await aioredis.create_redis_pool(REDIS_DSN)

    app['redis'] = redis
    app['storage'] = Storage(STORAGE_NAME, redis=redis)
    app['converter'] = Converter(storage=app['storage'])


async def stop_redis(app):
    app['redis'].close()
    await app['redis'].wait_closed()


def create_app():
    app = web.Application()
    app.on_startup.append(start_redis)
    app.on_shutdown.append(stop_redis)

    app.add_routes([
        web.get('/convert', convert),
        web.post('/database', database),
    ])

    return app


if __name__ == '__main__':
    uvloop.install()
    app = create_app()
    web.run_app(app)

from aiohttp import web
import aioredis

from config import REDIS_DSN, STORAGE_NAME
from storage import Storage
from views import *


def start_redis(redis=None):
    async def _start_redis(app):
        nonlocal redis

        if not redis:
            redis = await aioredis.create_redis_pool(REDIS_DSN)

        app['redis'] = redis
        app['storage'] = Storage(STORAGE_NAME, redis=redis)

    return _start_redis


async def stop_redis(app):
    app['redis'].close()
    await app['redis'].wait_closed()


def create_app(redis=None):
    app = web.Application()
    app.on_startup.append(start_redis(redis))
    app.on_shutdown.append(stop_redis)

    app.add_routes([
        web.get('/convert', convert),
        web.post('/database', database),
    ])

    return app


if __name__ == '__main__':
    app = create_app()
    web.run_app(app)

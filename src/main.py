from aiohttp import web
import aioredis

from config import REDIS_DSN, STORAGE_NAME
from storage import Storage


async def convert(request):
    return web.Response()


async def database(request):
    return web.Response()


async def start_redis(app):
    app['redis'] = await aioredis.create_redis_pool(REDIS_DSN)
    app['storage'] = Storage(STORAGE_NAME, redis=app['redis'])


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
    app = create_app()
    web.run_app(app)

from aiohttp import web


async def convert(request):
    return web.Response()


async def database(request):
    return web.Response()


async def create_app():
    app = web.Application()

    app.add_routes([
        web.get('/convert', convert),
        web.post('/database', database),
    ])

    return app


if __name__ == '__main__':
    app = create_app()
    web.run_app(app)

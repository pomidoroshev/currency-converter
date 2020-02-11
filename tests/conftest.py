from unittest import mock

# import aioredis
# import mockaioredis
import pytest

from config import REDIS_DSN, STORAGE_NAME
from main import create_app


@pytest.fixture
def cli(loop, aiohttp_client):
    app = create_app()
    return loop.run_until_complete(aiohttp_client(app))


@pytest.fixture
async def redis():
    return await aioredis.create_redis_pool(REDIS_DSN)


@pytest.fixture
async def detele_storage(redis):
    yield
    await redis.delete(STORAGE_NAME)


# @pytest.fixture(autouse=True)
# def redis():
#     with mock.patch.object(aioredis, 'create_redis_pool', new=mockaioredis.create_redis_pool) as m:
#         yield m

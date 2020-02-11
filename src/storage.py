__all__ = ('Storage',)


class Storage:
    def __init__(self, name, *, redis):
        self.name = name
        self.redis = redis

    async def set(self, key, value):
        await self.redis.hset(self.name, key, value)

    async def get(self, key):
        return await self.redis.hget(self.name, key)

    async def clear(self):
        return await self.redis.delete(self.name)

__all__ = ('Storage',)


class Storage:
    def __init__(self, name, *, redis):
        self.name = name
        self.redis = redis

    async def set(self, key, value):
        await self.redis.hset(self.name, key, value)

    async def get(self, key) -> str:
        res = await self.redis.hget(self.name, key)
        if not res:
            return ''
        return res.decode()

    async def clear(self):
        return await self.redis.delete(self.name)

    async def rewrite(self, data):
        tr = self.redis.multi_exec()
        tr.delete(self.name)
        if data:
            tr.hmset_dict(self.name, data)
        await tr.execute()

    async def update(self, data):
        if data:
            await self.redis.hmset_dict(self.name, data)

__all__ = ('Storage',)


class Storage:
    def __init__(self, name, *, redis):
        self.name = name
        self.redis = redis

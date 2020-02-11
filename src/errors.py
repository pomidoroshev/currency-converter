__all__ = ('UnknownCurrencyError',)


class UnknownCurrencyError(Exception):
    def __init__(self, currency):
        super().__init__('Unknown currency: %s' % currency)

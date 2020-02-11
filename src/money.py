from decimal import Decimal, ROUND_HALF_UP

__all__ = ('Money',)

class Money:
    def __init__(self, amount, currency):
        self.amount = Decimal(amount)
        self.currency = currency

    def to_json(self):
        return {
            'amount': self.amount.quantize(Decimal('0.01'), ROUND_HALF_UP),
            'currency': self.currency,
        }

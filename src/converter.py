from decimal import Decimal
from typing import Dict, List

from money import Money

__all__ = ('Converter',)

BASE_CURRENCY = 'RUR'
BASE_RATE = Decimal(1.0)

class Converter:
    def __init__(self, *, storage):
        self.storage = storage

    async def convert(self, money: Money, to_currency: str) -> Money:
        if money.currency == to_currency or not money.amount:
            return Money(money.amount, to_currency)

        current_rate = BASE_RATE
        to_rate = BASE_RATE

        if money.currency != BASE_CURRENCY:
            current_rate = Decimal(await self.storage.get(money.currency))

        if to_currency != BASE_CURRENCY:
            to_rate = Decimal(await self.storage.get(to_currency))

        amount = money.amount * current_rate / to_rate
        return Money(amount, to_currency)

    async def update(self, entries: List[Dict], merge: bool):
        if not merge:
            await self.storage.clear()

        for entry in entries:
            await self.storage.set(entry['currency'], str(entry['rate']))

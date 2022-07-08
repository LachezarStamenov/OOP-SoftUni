# HotBeverage and ColdBeverage are beverages.
from .beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price, milliliters)


# Beverage and Food classes are products:
# •	The Beverage class should have an additional private attribute – milliliters: float and its subsequent getter
# •	The Food class should have an additional private attribute – grams: float and its subsequent getter
from ..product import Product


class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters


# Beverage and Food classes are products:
# •	The Beverage class should have an additional private attribute – milliliters: float and its subsequent getter
# •	The Food class should have an additional private attribute – grams: float and its subsequent getter
from ..product import Product


class Food(Product):

    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        self.__grams = grams

    @property
    def grams(self):
        return self.__grams

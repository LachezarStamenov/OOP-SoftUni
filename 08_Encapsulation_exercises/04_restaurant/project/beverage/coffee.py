# Coffee and Tea are hot beverages:
# •	The Coffee class should have an additional private attribute – caffeine: float and its subsequent getter.
# It should also have the following class attributes, which should apply to all coffees made:
# o	MILLILITERS = 50 (constant)
# o	PRICE = 3.50 (constant)
from .hot_beverage import HotBeverage


class Coffee(HotBeverage):

    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

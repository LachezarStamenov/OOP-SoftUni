# Coffee and Tea are hot beverages:
# •	The Coffee class should have an additional private attribute – caffeine: float and its subsequent getter.
# It should also have the following class attributes, which should apply to all coffees made:
# o	MILLILITERS = 50 (constant)
# o	PRICE = 3.50 (constant)
from .hot_beverage import HotBeverage


class Tea(HotBeverage):

    def __init(self, name: str, price: float, milliliters: float):
        super().__init__(name, price, milliliters)

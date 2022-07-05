# In the file drink.py, the class Drink should be implemented. The class should inherit from the Product class.
# An instance of the Drink class will have a name and a quantity of 10.

from .product import Product


class Drink(Product):
    DEFAULT_QUANTITY = 10

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_QUANTITY)

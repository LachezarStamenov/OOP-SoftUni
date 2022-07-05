# In the food.py file, the Food class should be implemented. The class should inherit from the Product class.
# An instance of the Food class will have a name and a quantity of 15.
from .product import Product


class Food(Product):
    DEFAULT_QUANTITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_QUANTITY)

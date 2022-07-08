# The Product class should have the following private attributes and subsequent getters:
# •	name: string
# •	price: float

class Product:

    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

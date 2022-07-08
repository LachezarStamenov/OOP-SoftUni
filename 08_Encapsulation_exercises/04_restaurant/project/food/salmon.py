#  Salmon is a main dish. Also, it must have the following class attribute, which should apply to all salmons:
# o	GRAMS = 22 (constant)

from .main_dish import MainDish


class Salmon(MainDish):

    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, Salmon.GRAMS)

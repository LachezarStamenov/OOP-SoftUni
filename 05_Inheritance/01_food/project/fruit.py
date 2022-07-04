# In a folder called project create two files: food.py and fruit.py:
# •	In the food.py file, create a class called Food which will receive an expiration_date (str) upon initialization.
# •	In the fruit.py file, create a class called Fruit with will receive a name (str) and an expiration_date (str) upon
# initialization.
# Fruit should inherit from Food.
from project.food import Food


class Fruit(Food):

    def __init__(self, name: str, expiration_date):
        super().__init__(expiration_date)
        self.name = name

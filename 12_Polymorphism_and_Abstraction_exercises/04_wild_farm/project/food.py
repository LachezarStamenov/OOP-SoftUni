# Your task is to create a class hierarchy like the one described below. The Animal, Bird, Mammal, and Food classes
# should be abstract:
# In the food.py file, implement the following classes:
# •	Food - the class should be abstract and should receive quantity (int) upon initialization
# •	Vegetable, Fruit, Meat and Seed classes should inherit from the Food class


from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)
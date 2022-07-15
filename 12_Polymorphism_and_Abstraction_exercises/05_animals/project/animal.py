# Your task is to create a class hierarchy like the one described below. Submit in judge a zip file named project,
# containing a separate file for each of the classes.
# The Animal class (abstract) should take, as attributes, a name, an age, and a gender. It should have 2 methods: repr()
# and make_sound().

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

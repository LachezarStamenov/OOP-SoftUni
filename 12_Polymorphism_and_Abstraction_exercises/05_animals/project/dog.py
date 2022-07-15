# The Dog class should inherit and implement the Animal class. Its repr() method should return "This is {name}.
# {name} is a {age} year old {gender} {class}". The dog sound is "Woof!".
from .animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Woof!"
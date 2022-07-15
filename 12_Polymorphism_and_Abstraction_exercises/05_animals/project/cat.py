# The Cat class should inherit and implement the Animal class. Its repr() method should return "This is {name}.
# {name} is a {age} year old {gender} {class}". The cat sound, "Meow meow!".
from .animal import Animal


class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow meow!"

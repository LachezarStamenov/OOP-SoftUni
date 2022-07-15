# The Kitten class should inherit and implement the Cat class. Its gender is "Female", and its sound is "Meow".

from .cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def make_sound(self):
        return 'Meow'
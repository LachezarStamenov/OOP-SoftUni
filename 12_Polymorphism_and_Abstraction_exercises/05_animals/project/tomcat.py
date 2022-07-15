# The Tomcat class should inherit and implement the Cat class. Its gender is "Male", and its sound is "Hiss".
from .cat import Cat

class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def make_sound(self):
        return 'Hiss'
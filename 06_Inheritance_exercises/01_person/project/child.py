# You are asked to model an application for storing data about people. You should be able to have a Person and a
# Child. Every person receives name and age upon initialization. Your task is to model the application.
# Create a Child class that inherits Person and has the same constructor definition. However, do not copy the code
# from the Person class - reuse the Person class's constructor.
from .person import Person


class Child(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        
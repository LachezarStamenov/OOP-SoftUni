# Create a separate file for each class as shown below and submit a zip file containing all files (zip the whole
# project folder/module) - it is important to include all files in the project module to make proper imports.
# The Animal class is a base class for any type of animal in the zoo. It should receive four public attributes - a
# name (string), a gender (str), an age (int), and a money_for_care (int) upon initialization.
# The Animal class should also have 1 additional method:
# •	__repr__() - returns string representation of the animal in the format: "Name: {name}, Age: {age}, Gender: {gender}"
# The Lion, the Tiger, and the Cheetah classes should inherit from the Animal class. Each of these animals costs a
# certain amount of money to be cared for:
# •	A lion needs 50
# •	A tiger needs 45
# •	A cheetah needs 60

class Animal:

    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
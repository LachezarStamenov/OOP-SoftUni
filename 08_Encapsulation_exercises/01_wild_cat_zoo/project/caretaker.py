# The Keeper, the Caretaker, and the Vet classes should inherit from the Worker class.
from .worker import Worker


class Caretaker(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

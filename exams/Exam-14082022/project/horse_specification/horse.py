from abc import ABC, abstractmethod

from project.core.validator import Validator


class Horse(ABC):
    MIN_NUM_CHARS = 4
    SPEED_INCREASES = 0

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_less_than_min_numbers_of_chars(
            value,
            self.MIN_NUM_CHARS,
            f"Horse name {value} is less than {self.MIN_NUM_CHARS} symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.max_speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @property
    @abstractmethod
    def max_speed(self):
        pass

    def train(self):
        if self.speed + self.SPEED_INCREASES > self.max_speed:
            self.speed = self.max_speed
            return self.speed
        else:
            self.speed += self.SPEED_INCREASES
            return self.speed



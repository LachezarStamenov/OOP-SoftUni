from .movie import Movie
from ..core.validator import Validator


class Action(Movie):
    def __init__(self, title: str, year: int, owner, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validator.raise_if_number_is_less_than_restriction(
            value, 12, 'Action movies must be restricted for audience under 12 years!'
        )
        self.__age_restriction = value

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"

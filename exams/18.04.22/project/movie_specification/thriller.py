from movie_specification.movie import Movie
from core.validator import Validator


class Thriller(Movie):
    def __init__(self, title: str, year: int, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validator.raise_if_number_is_less_than_restriction(
            value, 16, "Thriller movies must be restricted for audience under 16 years!"
        )
        self.__age_restriction = value

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, " \
               f"Owned by:{self.owner.username}"

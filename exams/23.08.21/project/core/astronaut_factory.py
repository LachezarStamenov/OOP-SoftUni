from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautFactory:

    @staticmethod
    def create_astronaut(astronaut_type, name) -> Astronaut:
        if astronaut_type == "Biologist":
            return Biologist(name)
        elif astronaut_type == "Geodesist":
            return Geodesist(name)
        elif astronaut_type == "Meteorologist":
            return Meteorologist(name)
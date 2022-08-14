from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    SPEED_INCREASES = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 120

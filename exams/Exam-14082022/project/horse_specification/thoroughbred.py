from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    SPEED_INCREASES = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.speed = speed

    @property
    def max_speed(self):
        return 140

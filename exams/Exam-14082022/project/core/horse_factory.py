from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseFactory:
    horse_types = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    @staticmethod
    def create_horse(horse_type, horse_name, horse_speed):
        return HorseFactory.horse_types[horse_type](horse_name, horse_speed)

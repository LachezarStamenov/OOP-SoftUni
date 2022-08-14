from project.core.horse_factory import HorseFactory
from project.horse_race import HorseRace
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = HorseFactory.create_horse(horse_type, horse_name, horse_speed)
        if self.__check_if_horse_exist(horse_name):
            raise Exception(F"Horse {horse_name} has been already added!")
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = Jockey(jockey_name, age)
        for j in self.jockeys:
            if j.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        horse_race = HorseRace(race_type)
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = self.__find_last_horse_of_the_given_type_added(horse_type)
        jockey = self.__find_jockey(jockey_name)

        if not horse.is_taken and jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey.name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.__check_if_horse_race_exist(race_type)
        jockey = self.__find_jockey(jockey_name)

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        for jockey in horse_race.jockeys:
            if jockey.name == jockey_name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.__check_if_horse_race_exist(race_type)
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        highest_speed = 0
        jockey_name = None
        horse_name = None

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                jockey_name = jockey.name
                horse_name = jockey.horse.name


        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}!" \
               f" Winner's horse: {horse_name}."

    def __check_if_horse_exist(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return True
        return False

    def __find_last_horse_of_the_given_type_added(self, horse_type):
        for idx in range(len(self.horses) -1, -1, -1):
            horse = self.horses[idx]

            if horse.__class__.__name__ == horse_type:
                return horse
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def __find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def __check_if_horse_race_exist(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race
        raise Exception(f"Race {race_type} could not be found!")




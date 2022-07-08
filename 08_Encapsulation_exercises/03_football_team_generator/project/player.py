# Create a separate file for each class as shown below and submit a zip file containing all files (zip the whole
# project folder/module) - it is important to include all files in the project module to make proper imports.
# Create a class called Player. Upon initialization, it should receive:
# •	Private attribute name: string
# •	Private attribute sprint: int
# •	Private attribute dribble: int
# •	Private attribute passing: int
# •	Private attribute shooting: int
# You should create property only for the name of the player. The class should also have one additional method:
# Override the __str__() method of the class so it returns:
# "Player: {name}
# Sprint: {sprint}
# Dribble: {dribble}
# Passing: {passing}
# Shooting: {shooting}"

class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Player: {self.name}\n" + \
            f'Sprint: {self.__sprint}\n' + \
            f'Dribble: {self.__dribble}\n' + \
            f'Passing: {self.__passing}\n' + \
            f'Shooting: {self.__shooting}\n'

# Create a class called Team. Upon initialization, it should receive:
# •	Private attribute name: string
# •	Private attribute rating: int
# The class should also have a private instance attribute - players: list - empty list upon initialization that will
# contain all the players (objects)
# The Team class have the following methods:
# •	add_player(player: Player)
# o	If the player is already in the team, return "Player {name} has already joined"
# o	Otherwise, add the player to the team and return "Player {name} joined team {team_name}"
# •	remove_player(player_name: str)
# o	Remove the player and return him
# o	If the player is not in the team, return "Player {player_name} not found"
from .player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        for team_player in self.__players:
            if team_player.name == player.name:
                return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player
        return f"Player {player_name} not found"

from project.core.aquarium_factory import AquariumFactory
from project.core.decoration_factory import DecorationFactory
from project.core.fish_factory import FishFactory
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_aquarium_types = ['FreshwaterAquarium', 'SaltwaterAquarium']
        if aquarium_type not in valid_aquarium_types:
            return "Invalid aquarium type."
        new_aquarium = AquariumFactory.create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        valid_decoration_types = ['Plant', 'Ornament']
        if decoration_type not in valid_decoration_types:
            return 'Invalid decoration type.'
        new_decoration = DecorationFactory.create_decoration(decoration_type)
        self.decorations_repository.add(new_decoration)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish_types = ['FreshwaterFish', 'SaltwaterFish']
        if fish_type not in valid_fish_types:
            return f"There isn't a fish of type {fish_type}."

        fish = FishFactory.create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        sum_decorations = sum([d.price for d in aquarium.decorations])
        sum_fish = sum([f.price for f in aquarium.fish])
        total_value = sum_decorations + sum_fish

        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        output = ""

        for aquarium in self.aquariums:
            output += str(aquarium) + '\n'

        return output.strip()

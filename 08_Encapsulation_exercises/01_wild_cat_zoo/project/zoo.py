# The Zoo class should receive 4 attributes upon initialization:
# •	Public attribute name: string
# •	Private attribute budget: int
# •	Private attribute animal_capacity: int
# •	Private attribute workers_capacity: int
# It should also have 2 instance attributes:
# •	Public attribute animals: list - (empty upon initialization)
# •	Public attribute workers: list - (empty upon initialization)
# The Zoo class should also have 8 methods:
# •	add_animal(animal, price)
# o	If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals' list,
# reduce the budget, and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
# o	If you have the capacity, but no budget, return "Not enough budget"
# o	In any other case, you do not have space, and you should return "Not enough space for animal"
# •	hire_worker(worker)
# o	If you have not exceeded the capacity of workers in the zoo for the worker (instance of Keeper/Caretaker/Vet),
# add him to the workers and return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
# o	Otherwise, return "Not enough space for worker"
# •	fire_worker(worker_name)
# o	If there is a worker with that name in the workers' list, remove him and return "{worker_name} fired successfully"
# o	Otherwise, return "There is no {worker_name} in the zoo"
# •	pay_workers()
# o	If you have enough budget to pay the workers (sum their salaries) pay them and return "You payed your workers.
# They are happy. Budget left: {left_budget}"
# o	Otherwise, return "You have no budget to pay your workers. They are unhappy"
# •	tend_animals()
# o	If you have enough budget to take care of the animals, reduce the budget and return "You tended all the animals.
# They are happy. Budget left: {left_budget}"
# o	Otherwise, return "You have no budget to tend the animals. They are unhappy."
# •	profit(amount)
# o	Increase the budget with the given amount of profit
# •	animals_status()
# o	Returns the following string (Hint: use the __repr__ methods of the animals to print them on the console):
# "You have {total_animals_count} animals
# ----- {amount_of_lions} Lions:
# {lion1}
# …
# {lionN}
# ----- {amount_of_tigers} Tigers:
# {tiger1}
# …
# {tigerN}
# ----- {amount_of_cheetahs} Cheetahs:
# {cheetah1}
# …
# {cheetahN}"
# •	workers_status()
# o	Returns the following string (Hint: use the __repr__ methods of the workers to print them on the console):
# "You have {total_workers_count} workers
# ----- {amount_of_keepers} Keepers:
# {keeper1}
# …
# {keeperN}
# ----- {amount_of_caretakers} Caretakers:
# {caretaker1}
# …
# {caretakerN}
# ----- {amount_of_vetes} Vets:
# {vet1}
# …
# {vetN}"
from .worker import Worker
from .animal import Animal


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return f"Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return f"Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return f'Not enough space for worker'
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = 0
        for worker in self.workers:
            needed_money += worker.salary
        if needed_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= needed_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = 0
        for animal in self.animals:
            needed_money += animal.money_for_care
        if needed_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        result += self.__build_entity_str(self.animals, 'Lion')
        result += self.__build_entity_str(self.animals, 'Tiger')
        result += self.__build_entity_str(self.animals, 'Cheetah')
        return result.strip()

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        result += self.__build_entity_str(self.workers, 'Keeper')
        result += self.__build_entity_str(self.workers, 'Caretaker')
        result += self.__build_entity_str(self.workers, 'Vet')
        return result.strip()

    def __build_entity_str(self, entities, entity_type):
        counter = 0
        result = ''

        for entity in entities:
            if entity.__class__.__name__ == entity_type:
                counter += 1
                result += repr(entity) + '\n'
        return f'----- {counter} {entity_type}s:\n' + result





























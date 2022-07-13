# Upon initialization, the class will receive the following parameters: name: str. The class should also have an id
# (autoincremented starting from 1). To do the incrementation, you should create a class attribute id equal to 1, which
# will keep the value of the id for the next trainer's id.
# Implement the __repr__ method so it returns the info about the trainer in the following format: "Trainer <{id}>
# {name}"
# Create a static method called get_next_id, which returns the id that will be given to the next trainer.
class Trainer:

    id = 1

    def __init__(self, name: str):
        self.id = Trainer.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        result = Trainer.id
        Trainer.id += 1
        return result

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
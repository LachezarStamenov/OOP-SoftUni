# Upon initialization, the class will receive the following parameters: name: str. Each equipment should also have an
# id (autoincremented, starting from 1). To do the incrementation, you should create a class attribute id equal to 1,
# which will keep the value of the id for the following equipment's id.
# Create a method called get_next_id, which returns the id that will be given to the following equipment.
# Implement the __repr__ method so it returns the info about the equipment in the following format: "Equipment <{id}>
# {name}"
# Create a static method called get_next_id, which returns the id that will be given to the following equipment.

class Equipment:

    id = 1

    def __init__(self, name: str):
        self.id = Equipment.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        result = Equipment.id
        Equipment.id += 1
        return result

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"


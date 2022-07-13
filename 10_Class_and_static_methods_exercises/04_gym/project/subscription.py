# Upon initialization, the class will receive the following parameters: date: str, customer_id: int, trainer_id: int,
# exercise_id: int. The class should also have an id (autoincremented starting from 1). To do the incrementation, you
# should create a class attribute id equal to 1, which will keep the value of the id for the next subscription's id.
# Implement the __repr__ method so it returns the info about the subscription in the following format: "Subscription
# <{id}> on {date}"
# Create a static method called get_next_id which returns the id that will be given to the next subscription
class Subscription:

    id = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.id = Subscription.get_next_id()
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id

    @staticmethod
    def get_next_id():
        result = Subscription.id
        Subscription.id += 1
        return result

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

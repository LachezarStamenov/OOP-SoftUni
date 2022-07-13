# Upon initialization, the class will not receive any parameters. However, it should have the following attributes:
# customers (empty  list of customer objects), trainers (empty list of trainer objects), equipment (empty list of
# equipment objects), plans (empty list of plan objects), subscriptions (empty list of subscription objects)
# Create the following methods:
# •	add_customer(customer: Customer) - add the customer in the customer list if the customer is not already in it
# •	add_trainer(trainer: Trainer) - add the trainer to the trainers' list, if the trainer is not already in it
# •	add_equipment(equipment: Equipment) - add the equipment to the equipment list, if the equipment is not already in it
# •	add_plan(plan: ExercisePlan) - add the plan to the plans' list, if the plan is not already in it
# •	add_subscription(subscription: Subscription) - add the subscription in the subscriptions list if the subscription
# is not already in it
# •	subscription_info(subscription_id: int) - get the subscription, the customer, the trainer, the equipment, and the
# plan. Then return their string representations each on a new line.

from .customer import Customer
from .trainer import Trainer
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        self.__add_entity(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        self.__add_entity(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        self.__add_entity(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_entity(self.plans, plan)

    def add_subscription(self, subscription: Subscription):
        self.__add_entity(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_entity_by_id(self.subscriptions, subscription_id)
        customer = self.__find_entity_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_entity_by_id(self.trainers, subscription.trainer_id)
        plan = self.__find_entity_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_entity_by_id(self.equipment, plan.equipment_id)

        return repr(subscription) + '\n' + \
               repr(customer) + '\n' + \
               repr(trainer) + '\n' + \
               repr(equipment) + '\n' + \
               repr(plan)
        
    def __add_entity(self, collection, entity):
        if entity in collection:
            return
        collection.append(entity)

    def __find_entity_by_id(self, colection, entity_id):
        for entity in colection:
            if entity.id == entity_id:
                return entity








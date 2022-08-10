from project.drink.tea import Tea
from project.drink.water import Water


class DrinkFactory:
    drink_type = {
        'Tea': Tea,
        'Water': Water
    }

    @staticmethod
    def create_drink(drink_type, name, portion, brand):
        return DrinkFactory.drink_type[drink_type](name, portion, brand)

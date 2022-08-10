
from project.baked_food.bread import Bread
from project.bakery import Bakery

from project.drink.tea import Tea
from project.table.inside_table import InsideTable

bakery = Bakery('Test')
bakery.add_food('Bread', 'bread', 20)

bakery.add_drink("Tea", 'tea', 20, 'fddf')

bakery.add_table('InsideTable', 1, 5)
print(bakery.reserve_table(4))
# print(bakery.order_drink(1, 'tea', 'bread'))
print(bakery.order_drink(1, 'tea'))
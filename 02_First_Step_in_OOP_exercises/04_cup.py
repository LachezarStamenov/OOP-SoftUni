# Create a class called Cup. Upon initialization, it should receive size (integer) and quantity (an integer
# representing how much liquid is in it).
# The class should have two methods:
# •	fill(quantity) that will increase the amount of liquid in the cup with the given quantity (if there is space in
# the cup, otherwise ignore).
# •	status() that will return the amount of free space left in the cup.
# Submit only the class in the judge system. Do not forget to test your code.

class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        free_space = self.size - self.quantity
        if free_space >= quantity:
            self.quantity += quantity

    def status(self):
        free_space = self.size - self.quantity
        return free_space

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

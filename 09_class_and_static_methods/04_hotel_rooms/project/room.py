# In a folder called project create two files: hotel.py and room.py
# In the room.py file, create a class called Room. Upon initialization, it should receive a number (int) and a
# capacity (int). It should also have an attribute called guests (0 by default) and is_taken (False by default).
# The class should have 2 additional methods:
# •	take_room(people) - if the room is not taken, and there is enough space, the guests take the room. Otherwise,
# the method should return "Room number {number} cannot be taken"
# •	free_room() - if the room is taken, free it. Otherwise, return "Room number {number} is not taken"

class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if not self.is_taken and self.capacity >= people:
            self.is_taken = True
            self.guests = people
            return
        return f"Room number {self.number} cannot be taken"


    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
            return
        return f"Room number {self.number} is not taken"
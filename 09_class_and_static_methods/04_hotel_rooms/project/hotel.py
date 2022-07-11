# In the hotel.py file, create a class called Hotel. Upon initialization, it should receive a name (str). It should
# also have 2 more attributes: rooms (empty list of rooms) and guests (0 by default). The class should have 5 more
# methods:
# •	from_stars(stars_count: int) - creates a new instance with name "{stars_count} stars Hotel"
# •	add_room(room: Room) - adds the room to the list of rooms
# •	take_room(room_number, people) - finds the room with that number and tries to accommodate the guests in the room
# •	free_room(room_number) - finds the room with that number and tries to free it
# •	status() - returns information about the hotel in the following format:
# "Hotel {name} has {guests} total guests
# Free rooms: {numbers of all free rooms separated by comma and space}
# Taken rooms: {numbers of all taken rooms separated by comma and space}"
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self):
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(str(x) for x in free_rooms)}" \
               f"\nTaken rooms: {', '.join(str(x) for x in taken_rooms)}"



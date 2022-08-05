# Create a HashTable class that should have the needed functionality for a hash table, such as:
# •	hash(key: str) - a function that should figure out where to store the key-value pair
# •	add(key: str, value: any) - adds a new key-value pair usign the hash function
# •	get(key: str) - returns the value corresponding to the given key
# •	additional "magic" methods, that will make the code in the example work correctrly
# The HashTable should have an attribute called array of type: list, where all the values will be stored.
# Upon initialization the default length of the array should be 4. After each addition of an element if the
# HashTable gets too populated, double the length of the array and re-add the existing data.
# You are not allowed to inherit any classes. Feel free to implement your own functionality (and unit tests) or to
# write the methods by yourself.
from copy import copy


class HashTable:
    DEFAULT_CAPACITY = 4

    def __init__(self):
        self.data = [None] * self.DEFAULT_CAPACITY
        self.free_slots = self.DEFAULT_CAPACITY
        self.items_count = 0

    def add(self, key, value):
        if self.free_slots == 0:
            self.grow_data()

        idx = self.calc_idx(key)
        if self.data[idx] is None:
            self.data[idx] = [(key, value)]
            self.free_slots -= 1
            self.items_count += 1
            return
        for k, _ in self.data[idx]:
            if key == k:
                raise KeyError(f'{key} not found!')
        self.data[idx].append((key, value))

    def calc_idx(self, key):
        return hash(key) % len(self.data)

    def __len__(self):
        return self.items_count

    def get(self, key):
        idx = self.calc_idx(key)
        idx_elements = self.data[idx]
        if idx_elements is None:
            raise KeyError(f'{key} not found!')

        for k, v in idx_elements:
            if k == key:
                return v
            raise KeyError(f'{key} not found!')

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        try:
            old_value = self.get(key)
            idx = self.calc_idx(key)
            self.data[idx].remove(key, old_value)
            self.data[idx].append(key, value)
        except KeyError:
            self.add(key, value)

    def remove(self, key):
        idx = self.calc_idx(key)
        idx_elements = self.data[idx]
        if idx_elements is None:
            raise KeyError(f'{key} does not exist!')

        for k, v in idx_elements:
            if k == key:
                self.data[idx].remove((k, v))
                return
        raise KeyError(f'{key} does not exist!')

    def grow_data(self):
        new_capacity = len(self.data) * 2

        existing_data = copy(self.data)

        self.free_slots = new_capacity
        self.data = [None] * new_capacity
        self.items_count = 0

        for slot in existing_data:
            for key, value in slot:
                self.add(key, value)



table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))

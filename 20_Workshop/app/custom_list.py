# In this workshop, we are going to create a custom data structure, which has similar functionalities as the Python
# List and create unit tests for its functionalities. It will have the same functionalities as the original List:
# •	append(value) - Adds a value to the end of the list. Returns the list.
# •	remove(index) - Removes the value on the index. Returns the value removed.
# •	get(index) - Returns the value on the index.
# •	extend(iterable) - Appends the iterable to the list. Returns the new list.
# •	insert(index, value) - Adds the value on the specific index. Returns the list.
# •	pop() - Removes the last value and returns it.
# •	clear() - Removes all values, contained in the list.
# •	index(value) - Returns the index of the given value.
# •	count(value) - Returns the number of times the value is contained in the list.
# •	reverse() - Returns the values of the list in reverse order.
# •	copy() - Returns a copy of the list.
#
# We will also add our own custom functionalities:
# •	size() - Returns the length of the list.
# •	add_first(value) - Adds the value at the beginning of the list
# •	dictionize() - Returns the list as a dictionary: The keys will be each value on an even position and their values
# will be each value on an odd position. If the last value on an even position, it’s value will be " " (space)
# •	move(amount) - Move the first "amount" of values to the end of the list. Returns the list.
# •	sum() - Returns the sum of the list. If the value is not a number, add the length of the value to the overall
# number.
# •	overbound() - Returns the index of the biggest value. If the value is not a number, check it’s length.
# •	underbound() - Returns the index of the smallest value. If the value is not a number, check it’s length.
#
# Do not inherit List. Feel free to implement your own functionality (and unit tests) or to write the methods by
# yourself.

from copy import deepcopy


class CustomIntList:
    def __init__(self):
        self.__values = []

    def append(self, value):
        if not isinstance(value, int):
            raise ValueError("Only ints accepted")
        self.__values.append(value)
        return self.__values

    def remove(self, index):
        try:
            element = self.__values.pop(index)
            return element
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer")

    def get(self, index):
        try:
            el = self.__values[index]
            return el
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer")

    def extend(self, values):
        try:
            for el in values:
                if not isinstance(el, int):
                    raise ValueError("Only ints accepted")
            self.__values.extend(values)
            return deepcopy(self.__values)
        except TypeError:
            raise ValueError("Extend method works only with iterable objects")

    def insert(self, index, value):
        try:
            if index < 0 or index >= len(self.__values):
                raise IndexError
            self.__values.insert(index, value)
            return self.__values
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer")

    def pop(self):
        try:
            el = self.__values.pop()
            return el
        except IndexError:
            raise IndexError("No elements in list")

    def clear(self):
        self.__values.clear()

    def index_left(self, value):
        for index in range(len(self.__values)):
            el = self.__values[index]
            if el == value:
                return index
        raise ValueError("Value is not in list")

    def index_right(self, value):
        for index in range(len(self.__values) - 1, -1, -1):
            el = self.__values[index]
            if el == value:
                return index
        raise ValueError("Value is not in list")

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        if not isinstance(value, int):
            raise ValueError("Only ints accepted")
        self.__values.insert(0, value)

    def dictionize(self):
        result = {}
        for index in range(0, len(self.__values), 2):
            key = self.__values[index]
            val = self.__values[index + 1] if index < len(self.__values) - 1 else 0
            result[key] = val
        return result

    def move(self, amount):
        left_side = self.__values[:amount]
        right_side = self.__values[amount:]
        self.__values = right_side + left_side
        return self.__values

    def sum(self):
        return sum(self.__values)

    def overbound(self):
        return self.__values.index(max(self.__values))

    def underbound(self):
        return self.__values.index(min(self.__values))
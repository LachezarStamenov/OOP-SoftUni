# Create a class called sequence_repeat which should receive a sequence and a number upon initialization. Implement an
# iterator to return the given elements, so they form a string with a length - the given number. If the number is
# greater than the number of elements, then the sequence repeats as necessary.

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= self.number:
            raise StopIteration
        result = self.sequence[self.idx % len(self.sequence)]
        self.idx += 1
        return result

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')




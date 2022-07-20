# Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods, so the
# iterator returns only the vowels from the string.

class vowels:
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.all_vowels = 'AOEYUIaoeyui'
        self.vowels = [el for el in self.text if el in self.all_vowels]
        self.end = len(self.vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.vowels[index]

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

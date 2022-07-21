# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object.
# Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements
# (the key and the value).
class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary

        


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

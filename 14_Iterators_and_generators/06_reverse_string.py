# Create a generator function called reverse_text that receives a string and yields all string characters on one line
# in reversed order.
def reverse_text(string):
    start_index = len(string) - 1
    end_index = 0
    while start_index >= end_index:
        yield string[start_index]
        start_index -= 1


for char in reverse_text("step"):
    print(char, end='')

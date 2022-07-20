# Create a generator function called squares that should receive a number n. It should generate the squares of all
# numbers from 1 to n (inclusive).

def squares(n):
    current_num = 1

    while current_num <= n:
        yield current_num ** 2
        current_num += 1

print(list(squares(5)))
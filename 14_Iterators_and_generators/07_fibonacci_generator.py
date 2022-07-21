# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. The first two numbers
# in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current number
# with the previous one.
def fibonacci():
    fib0 = 0
    fib1 = 1

    yield fib0
    yield fib1
    while True:
        next_num = fib0 + fib1
        yield next_num
        fib0 = fib1
        fib1 = next_num


generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))


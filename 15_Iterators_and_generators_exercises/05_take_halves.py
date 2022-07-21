# Implement the three generator functions:
# •	integers() - generates an infinite amount of integers (starting from 1)
# •	halves() - generates the halves of those integers (each integer / 2)
# •	take(n, seq) - takes the first n halves of those integers
import numbers


def solution():

    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

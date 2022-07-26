# Create a decorator called cache. It should store all the returned values of the recursive function fibonacci.
# You are provided with this code:

def cache(func):
    memo = {}

    def wrapper(n):

        if n in memo:
            return memo[n]
        result = func(n)
        memo[n] = result
        return result
    wrapper.log = memo
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)


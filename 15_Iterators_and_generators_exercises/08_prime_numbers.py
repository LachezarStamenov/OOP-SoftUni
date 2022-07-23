# Create a generator function called get_primes() which should receive a list of integer numbers and return a list
# containing only the prime numbers from the initial list.

def is_prime(num):
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
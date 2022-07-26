# Create a decorator called store_results. It should return the name of the function that is being called and its parameters.
# It should also return the result of the execution of the function being called. See the examples for
# more clarification.

def logged(func_ref):
    def wrapper(*args):
        func_name = func_ref.__name__
        func_result = func_ref(*args)

        return f"you called {func_name}{args}\nit returned {func_result}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

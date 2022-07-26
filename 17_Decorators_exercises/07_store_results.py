# Create a class called store_results. It should be used as a decorator and store information about the executed
# functions in a file called results.txt in the format: "Function {func_name} was add called. Result: {func_result}"

def store_results(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        with open('./results.txt', 'a') as file:
            file.write(f"Function '{func_ref.__name__}' was called. Result: {result}")
            file.write('\n')
        return result
    return wrapper


@store_results
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
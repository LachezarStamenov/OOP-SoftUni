# Create three decorators: make_bold, make_italic, make_underline, which will have to wrap a text returned from a
# function in <b></b>, <i></i> and <u></u> respectively.


def make_bold(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return f'<b>{func_result}</b>'
    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return f'<i>{func_result}</i>'

    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return f'<u>{func_result}</u>'
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

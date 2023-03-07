
import functools


def decorator_function(fun):
    def decorated(*args):
        print("*"*10)
        fun(*args)
        print("*" * 10)
    return decorated

@decorator_function
def print_values(*args):
    for i in args:
        print(i)

print_values(1,2,3)



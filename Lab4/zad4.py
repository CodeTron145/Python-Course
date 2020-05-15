from inspect import getfullargspec
from math import sqrt
functions_dictionary = {}


def overload(function_to_decorate):

    functions_dictionary[(function_to_decorate.__name__,
                          len(getfullargspec(function_to_decorate).args))] = function_to_decorate

    def wrapper(*args, **kwargs):
        return functions_dictionary[(function_to_decorate.__name__,
                                     len(args) + len(kwargs))](*args, **kwargs)
    return wrapper


@overload
def norm(x, y):
    return sqrt(x * x + y * y)


@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)


print(f"norm(2,4) = {norm(2,4)}")
print(f"norm(2,3,4) = {norm(2,3,4)}")
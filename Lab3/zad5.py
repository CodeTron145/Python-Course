from functools import reduce

num = [1, 2, 3, 4, 5]


def powerset(arr):
    return reduce(lambda result, x: result + [subarr + [x] for subarr in result], arr, [[]])


print(powerset(num))
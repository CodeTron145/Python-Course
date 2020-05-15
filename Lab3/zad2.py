l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]


def flatten(l):
    for i in l:
        if type(i) == list:
            l = i
            yield from flatten(l)
        else:
            yield i


print(list(flatten(l)))
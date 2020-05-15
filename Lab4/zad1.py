import time


def calculate_time(func):

    def inner(num):
        begin = time.time()

        func(num)

        end = time.time()
        print("Czas działania funkcji", func.__name__, end - begin)

    return inner


@calculate_time
def adder(nums_array):

    print(sum(nums_array))


nums = [1, 2, 3, 4]
adder(nums)

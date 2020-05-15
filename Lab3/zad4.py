import random

nums = random.sample(range(20), 10)


def quick_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    pivot = arr[0]

    lt_pivot = list(filter(lambda x: (x < pivot), arr))
    qt_pivot = list(filter(lambda x: (x > pivot), arr))

    return quick_sort(lt_pivot) + [pivot] + quick_sort(qt_pivot)


print(quick_sort(nums))
file = "/home/valera/PycharmProjects/Lab3/plik.txt"


def num_bytes(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()

    split_subl = [i.split(' ') for i in lines]
    arr_b = [int(j) for i in split_subl for j in i if j == i[-1]]
    sum_b = sum(arr_b)
    print("Całkowita liczba bajtów: " + str(sum_b))


num_bytes(file)

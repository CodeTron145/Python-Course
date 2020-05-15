matrix = ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]


def transposition():
    matrix_trans = ([str(j) for k in range(len(matrix)) for i in matrix for j in i.split(' ') if
                    i.index(j) % len(matrix) - k == 0])
    matrix_trans = [matrix_trans[x:x+len(matrix)] for x in range(0, len(matrix)**2, len(matrix))]
    matrix_trans = [' '.join(sub_list) for sub_list in matrix_trans]
    print(matrix_trans)


transposition()
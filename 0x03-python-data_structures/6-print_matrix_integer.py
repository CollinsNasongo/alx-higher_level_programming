#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    ln = len(matrix) - 1

    while (i <= ln):
        for x in matrix[i]:
            print("{:d}".format(x), end='')
        i += 1
        print("$")

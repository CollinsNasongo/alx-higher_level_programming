#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # matrix is 2 dimensional
    square_matrix = [[i*i for i in x] for x in matrix]
    return square_matrix

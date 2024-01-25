#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(list(map(lambda i: i * i, row)) for row in matrix)
    return new_matrix

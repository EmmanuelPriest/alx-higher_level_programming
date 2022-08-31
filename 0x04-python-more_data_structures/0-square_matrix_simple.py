#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for row in matrix:
        new_matrix = [list(map(lambda x: (x ** 2), row))]
        return new_matrix

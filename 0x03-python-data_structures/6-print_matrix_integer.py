#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n in range(0, len(matrix), 3):
        print("{:d} {:d} {:d}$".format(*matrix[n: (n + 3)]))

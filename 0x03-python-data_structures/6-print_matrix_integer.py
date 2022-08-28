#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    m = (len(matrix) + 2) // 3
    for n in range(m):
        print("{:d} {:d} {:d}".format(*matrix[3 * n: (n + 1) * 3]))

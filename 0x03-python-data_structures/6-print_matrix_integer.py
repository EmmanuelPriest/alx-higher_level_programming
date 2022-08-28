#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        m = ('\t'.join(map(str, n)))
        print("{:d}".format(m))

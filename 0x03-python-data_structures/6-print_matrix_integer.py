#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    n = '\n'.join([''.join(['{: 2}'.format(item) for item in row] for row in
                           matrix]))
    print("{:d}".format(n))

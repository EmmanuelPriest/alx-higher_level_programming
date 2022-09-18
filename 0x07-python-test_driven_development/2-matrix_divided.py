#!/usr/bin/python3

'''Handling the division of all elements of a matrix by a number'''


def matrix_divided(matrix, div):
    '''Division of all elements of a matrix

    Args:
        matrix (list): List of list of integers or floats
        div (int or float): the divisor
    Raises:
        TypeError: If the matrix(list of lists) does not contain int/float
        TypeError: If each row of matrix is not of the same size
        TypeError: If div is not a number of int/float
        ZeroDivisionError: If div is equal to zero
    Returns:
        A new matrix

    '''
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, int) or isinstnace(elem, float))
                    for elem in [numb for row in matrix for numb in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) or not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda n: round(n / div, 2), row)) for row in matrix]

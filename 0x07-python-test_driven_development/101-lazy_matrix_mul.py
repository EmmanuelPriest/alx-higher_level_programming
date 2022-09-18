#!/usr/bin/python3

'''Handling lazy_matrix_mul function to multiply two matrices'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''Multiplying two matrices using numpy

    Args:
        m_a (list of lists of int/float): The fist matrix to be multiplied
        m_b (list of lists of int/float): The second matrix to be multiplied

    '''

    tan = np.dot(m_a, m_b)
    return tan

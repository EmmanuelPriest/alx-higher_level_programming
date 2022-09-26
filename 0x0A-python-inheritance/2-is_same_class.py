#!/usr/bin/python3

'''Defines the instance of an object of a given class'''


def is_same_class(obj, a_class):
    '''Returns the instance of an object of a given class

    Returns:
        True if object exists, False if otherwise

    '''
    if isinstance(obj, int):
        return True
    else:
        return False

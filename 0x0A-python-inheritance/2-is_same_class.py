#!/usr/bin/python3

'''Defines the instance of an object of a given class'''


def is_same_class(obj, a_class):
    '''Returns the instance of an object of a given class

    Args:
        obj (any): The object to be matched
        a_class (type): The type class that the object will match

    Returns:
        True if object exists, False if otherwise

    '''
    if type(obj) == (a_class):
        return True
    else:
        return False

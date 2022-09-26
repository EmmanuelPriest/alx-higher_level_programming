#!/usr/bin/python3

'''Defines an object that is an instance of a particular or inherited class'''


def is_kind_of_class(obj, a_class):
    '''Checks if an object is an instance of a particular or inherited class

    Args:
        obj (any): The object to be checked
        a_class (type): A particular or inherited class

    Returns:
        True if the obj is an instance of a particular or inherited class,
        otherwise False

    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False

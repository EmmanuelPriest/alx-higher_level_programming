#!/usr/bin/python3

'''Defines object of an instance a class inherited from a specified class'''


def inherits_from(obj, a_class):
    '''Checks for an instance a class inherited from a specified class

    Args:
        obj (any): The object to be checked
        a_class (type): The class inherited from a specified class

    Returns:
        True if object of an instance a class inherited from a specified class
        otherwise, False

    '''
    if issubclass(type(obj), a_class) and type(obj) != (a_class):
        return True
    else:
        return False

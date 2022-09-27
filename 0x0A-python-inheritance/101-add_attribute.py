#!/usr/bin/python3

'''Defines a method that adds attributes to object'''


def add_attribute(obj, att, value):
    '''Method that adds a new attribute to an object if possible.

    Args:
        obj (any): The object to be added to
        att (str): The name of the attribute to be added to object
        value (any): The value of attribute

    Raises:
        TypeError: If the object can't have new attribute

    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

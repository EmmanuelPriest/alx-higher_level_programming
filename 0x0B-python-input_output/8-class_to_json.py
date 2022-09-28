#!/usr/bin/python3

'''Defines a method that return dict description with simple data structure'''


def class_to_json(obj):
    '''Returns dict description with simple data structure

    Args:
        obj (any): The return object

    '''
    return obj.__dict__

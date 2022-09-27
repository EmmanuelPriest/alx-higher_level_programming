#!/usr/bin/python3

'''Defines a method that returns JSON representation of an object(string)'''
import json


def to_json_string(my_obj):
    '''Returns JSON representation of an object

    Args:
        my_obj (any): The object to be represented

    '''
    return json.dumps(my_obj)

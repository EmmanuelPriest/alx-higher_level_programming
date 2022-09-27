#!/usr/bin/python3

'''Defines a method that returns an object represented by a JSON string'''
import json


def from_json_string(my_str):
    '''Returns an object representated by a JSON string

    Args:
        my_str (any): The object to be represented

    '''
    return json.load(my_str)

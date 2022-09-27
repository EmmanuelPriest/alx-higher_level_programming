#!/usr/bin/python3

'''Defines a method that cretaes an object from a JSON file'''
import json


def load_from_json_file(filename):
    '''Creates an object a JSON file

    Args:
        filename (any): The needed json file

    '''
    with open(filename) as f:
        return json.load(f)

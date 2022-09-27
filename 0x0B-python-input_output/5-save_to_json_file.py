#!/usr/bin/python3

'''Defines method that writes an object to a text file using JSON rep'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an object to a text file

    Args:
        my_obj (any): The object to be written
        filename (str): The file to write to

    '''
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)

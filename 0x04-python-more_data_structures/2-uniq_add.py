#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    new_list = 0
    for x in set(my_list):
        new_list += x
    return new_list

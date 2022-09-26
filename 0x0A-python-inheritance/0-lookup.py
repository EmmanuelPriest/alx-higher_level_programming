#!/usr/bin/python3

'''Handles the listing of available attributes and methods of an object'''


def lookup(obj):
    '''Returns the list of available attributes and methods of an object

        Args:
            Obj (any): Object to be listed

    '''
    return dir(obj)

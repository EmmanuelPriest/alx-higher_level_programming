#!/usr/bin/python3

'''Defines a class that inherits a list'''


class MyList(list):
    '''A class that inherits a list'''

    def print_sorted(self):
        '''Prints a sorted list in ascending order'''
        print(sorted(self))

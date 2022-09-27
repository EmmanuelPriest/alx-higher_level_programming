#!/usr/bin/python3

'''Defines MyInt class module'''


class MyInt(int):
    '''MyInt class that inherits from int'''
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True

# class MyInt:
#     '''MyInt class that inherits from int'''

#     def __init__(self, integer):
#         self.integer = integer

#     def __str__(self):
#         return '{}'.format(self.integer)

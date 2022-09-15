#!/usr/bin/python3

'''class Square that defines a square'''


class Square:
    '''Creating the init method of class Square'''

    def __init__(self, size=0):
        '''Init method to initialize a square

        Args:
            size (int): The size of the new square.

        '''
        if not isinstance(size, int):
            raise TypeError
            print("size must be an integer")
        elif size < 0:
            raise ValueError
            print("size must be >= 0")
        self.__size = size

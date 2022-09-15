#!/usr/bin/python3

'''class Square that defines a square'''


class Square:
    '''Creating the init method of class Square'''

    def __init__(self, size=0):
        '''Init method to initialize square

        Args:
            size (int): The size of the square

        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Returns the current square area'''
        return (self.__size ** 2)

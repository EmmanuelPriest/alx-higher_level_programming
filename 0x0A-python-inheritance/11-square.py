#!/usr/bin/python3

'''Defines Square class that inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defines subclass of Rectangle Square'''

    def __init__(self, size):
        '''Initializes the Square sizes

        Args:
            size (int): The size of the square

        '''
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Returns area of the sqaure'''
        return self.__size ** 2

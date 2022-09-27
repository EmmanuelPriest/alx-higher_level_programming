#!/usr/bin/python3

'''Defines Rectangle class that inherits from BaseGeometry'''
Rectangle = __import__('9-rectangle').Rectangle


class Rectangle(BaseGeometry):
    '''Defines subclass of BaseGeometry Rectangle'''

    def __init__(self, size):
        '''Initializes the rectangle sizes

        Args:
            size (int): The size of the square

        '''
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        '''Returns area of the sqaure'''
        return self.__size ** 2

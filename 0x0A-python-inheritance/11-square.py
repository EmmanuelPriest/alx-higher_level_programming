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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

#!/usr/bin/python3

'''Defines Rectangle class that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Defines subclass of BaseGeometry Rectangle'''

    def __init__(self, width, height):
        '''Initializes the rectangle sizes

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        '''
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

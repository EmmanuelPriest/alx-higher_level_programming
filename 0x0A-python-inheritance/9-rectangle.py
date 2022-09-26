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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Return the area of the triangle'''
        return self.__width * self.__height

    def __str__(self):
        '''print and string representation of the rectangle'''
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

#!/usr/bin/python3

'''class Rectangle that defines rectangle'''


class Rectangle:
    '''Creating the init method of class Rectangle'''

    def __init__(self, width=0, height=0):
        '''Init method to initialize rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''int: Private attribute width

        Returns:
            Private attribute width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method that sets value into width, must be int

        Args:
            value (int): value(=width) of the rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value  #: value(=width) of the rectangle

    @property
    def def height(self):
        '''int: Private attribute height

        Returns:
            Private attribute height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method that sets value into height, must be an integer

        Args:
            value (int): value(=height) of the rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value  #: value(=height) of the rectangle

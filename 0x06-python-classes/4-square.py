#!/usr/bin/python3

'''class Square that defines a square'''


class Square:
    '''Creating the init method of class Square'''

    def __init__(self, size=0):
        '''Init method to initialize square

        Args:
            size (int): size of the square

        '''
        self.size = size

    @property
    def size(self):
        '''int: private attribute size

        Returns:
            Private attribute size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method that sets value into size, must be int

        Args:
            value (int): value(=size) of the square
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  #: value(=size) of the square

    def area(self):
        '''returns the current square area

        Returns:
            Area square

        '''
        return (self.__size ** 2)

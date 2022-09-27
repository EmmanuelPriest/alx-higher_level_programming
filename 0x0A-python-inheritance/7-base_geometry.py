#!/usr/bin/python3

'''Defines a class BaseGeometry'''


class BaseGeometry:
    '''Class that defines a method area'''

    def area(self):
        '''Defines geometric area

        Raises:
            Exception area() not implemented

        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method that validates value

        Args:
            name (str): The name used dynamically
            value (int): The value used

        Raises:
            TypeError if value is not an integer
            ValueError if value is less than or equal to 0

        '''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

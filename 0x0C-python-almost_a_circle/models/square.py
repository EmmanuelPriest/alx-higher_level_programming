#!/usr/bin/python3

'''Defines class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square that inherits from class Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes the init method of class Square

        Args:
            size (int): The size of the Square
            x (int): The x coordinate of the Square
            y (int): The y coordinate of the Square
            id (int): The identity of the Square

        '''
        super().__int__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter of the size of the Square'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter of the size of the Square'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Updating of the Square

        Args:
            *args (ints): List of arguments
                - 1st argument should be the id attribute
                - 2nd argument should be the size attribute
                - 3rd argument should be the x attribute
                - 4th argument should be the y attribute
            **kwargs (dict): Key/value pairs of attributes

        '''
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
                n += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        '''Return the dictionary representation of the Square'''
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        '''Return the print() and str() representation of the Square'''
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

#!/usr/bin/python3

'''Defines class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''class Rectangle that inherits class Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes the init method of class Rectangle

        Attributes:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
            x (int): The x coordinate of the Rectangle
            y (int): The y coordinate of the Rectangle
            id (int): The identity of Rectangle

        Raises:
            TypeError: If width or height is not an int
            TypeError: If x or y is not an int
            ValueError: If width or height is less than or equal to zero
            ValueError: If x or y is less than zero

        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Getter width method of the Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter width method of the Rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Getter height method of Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter height method of Rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        sel.__height = value

    @property
    def x(self):
        '''Getter x coordinate of the Rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter x coordinate of the Rectangle'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Getter y coordinate of the Rectangle'''
        return self.__y

    @y.setter
    '''Setter y coordinate of the Rectangle'''
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Returns the area of the Rectangle'''
        return (self.width * self.height)

    def display(self):
        '''Prints the Rectangle instance with the "#" character'''
        if self.with == 0 or self.height == 0:
            print("")

        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        '''Updating the Rectangle

        Args:
            *args (ints): The Rectangle attribute values
                - 1st argument should be id attribute
                - 2nd argument should be width attribute
                - 3rd argument should be height attribute
                - 4th arg should be x attribute
                - 5th argument should be y attribute
            **kwargs (dict): The key/value pair of Rectangle attributes

        '''
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.height = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
                n += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y == value

    def to_dictionary(self):
        '''Returns the dict representation of Rectangle'''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        '''Return the print() and str() representation of the Rectangle'''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -
        {self.width}/{self.height}"

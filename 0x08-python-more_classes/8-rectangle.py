#!/usr/bin/python3

'''class Rectangle that defines a square'''


class Rectangle:
    '''Creating init method of class
    Attributes:
        number_of_instances (int): The number of Rectangle instance created
        print_symbol (any): The symbol for string representation
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Init method to initialize square

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        '''int: Private attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''int: Private attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns the rectangle area

        Returns:
            Rectangle area

        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Returns the rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        perim = 2 * (self.__width + self.__height)
        return perim

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on the area
        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle

        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1

    def __str__(self):
        '''Returns the printed rectangle with the character "#"

        '''
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for n in range(self.__height):
            for m in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if n != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        '''Returns a string representation of the rectangle

        '''
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        '''Returns a string when an instance of Rectangle is deleted

        '''
        type(self).number_of_instances -= 1
        del self.__height
        print("Bye rectangle...")

#!/usr/bin/python3

'''class Square that defines a square'''


class Square:
    '''Creating the init method of class Square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Init method to initialize square

        Args:
            size (int): size of the square
            position (int of tuple): position of the square

        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''int: private attribute size

        Returns:
            Private attribute size
        '''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''int of tuple: private attribute position

        Returns:
            Private attribute position
        '''
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num_pos, int) for num_pos in value) or
                not all(num_pos >= 0 for num_pos in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''returns the current square area

        Returns:
            Area square

        '''
        return (self.__size ** 2)

    def my_print(self):
        '''Method that prints the square with the # character'''
        if self.__size == 0:
            print("")
            return

        for n in range(0, self.__position[1]):
            print("")
            for n in range(0, self.__size):
                for m in range(0, self.__position[0]):
                    print(" ", end="")
                    for x in range(0, self.__size):
                        print("#", end="")
        print("")

#!/usr/bin/python3
'''class Square that defines a square'''


class Square:
    '''class Square to create private attribute'''
    def __init__(self, size):
        '''Init method to initialize square

        Args:
            size (int): size of the square

        '''
        self.__size = size  #: size of the square

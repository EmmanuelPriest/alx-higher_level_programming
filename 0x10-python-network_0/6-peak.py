#!/usr/bin/python3

'''Defines a function that finds a peak in a list of unsorted integers'''


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): List of integers to find a peak from
    '''
    low = len(list_of_integers)
    high = low
    middle = low // 2

    if low == 0:
        return None

    while True:
        high //= 2
        if (middle < low - 1 and
                list_of_integers[middle] < list_of_integers[middle + 1]):
            if high // 2 == 0:
                high = 2
            middle = middle + high // 2
        elif high > 0 and list_of_integers[middle] <\
                list_of_integers[middle - 1]:
            if high // 2 == 0:
                high = 2
            middle = middle - high // 2
        else:
            return list_of_integers[middle]

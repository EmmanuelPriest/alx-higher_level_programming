#!/usr/bin/python3

'''Defines a function that finds a peak in a list of unsorted integers'''


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): List of integers to find a peak from
    '''
    if list_of_integers is None or list_of_integers == []:
        return None
    low = 0
    high = len(list_of_integers)
    middle = int(((high - low) // 2) + low)

    if high == 1:
        return list_of_integers[0]
    if high == 2:
        return max(list_of_integers)
    if list_of_integers[middle] >= list_of_integers[middle - 1]\
            and list_of_integers[middle] >= list_of_integers[middle + 1]:
        return list_of_integers[middle]
    if middle > 0 and list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle:])
    if middle > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])

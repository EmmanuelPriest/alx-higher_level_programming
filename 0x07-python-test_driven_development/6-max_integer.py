#!/usr/bin/python3

'''Module to find the max integer in a list'''


def max_integer(list=[]):
    '''Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    '''
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

result = max_integer([0, 2 + 5j, -3, 4, "Hello", 3.65, True])
print(result)
print(max_integer([1, 3, 4, 2]))

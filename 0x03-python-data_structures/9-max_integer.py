#!/usr/bin/python3

def max_integer(my_list=[]):
    max_int = my_list[0]
    for n in my_list:
        if len(my_list) == 0:
            return None
        elif n > max_int:
            max_int = n
        else:
            return max_int

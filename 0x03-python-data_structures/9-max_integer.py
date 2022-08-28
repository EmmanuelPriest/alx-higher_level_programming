#!/usr/bin/python3

def max_integer(my_list=[]):
    max_int = my_list[0]
    for n in my_list:
        if n > max_int:
            max_int = n
        else:
            return None

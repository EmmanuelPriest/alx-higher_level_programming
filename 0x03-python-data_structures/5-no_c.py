#!/usr/bin/python3

def no_c(my_string):
    new_my_string = my_string.translate({ord(n): None for n in "cC"})
    return new_my_string

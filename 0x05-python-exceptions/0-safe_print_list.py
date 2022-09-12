#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for x in my_list:
        try:
            if x > len(my_list):
                return x
            except IndexError:
                print(x, end='')

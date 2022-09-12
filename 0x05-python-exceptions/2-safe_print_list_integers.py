#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    real_number = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            real_number += 1
        except IndexError:
            pass
    print("")
    return real_number

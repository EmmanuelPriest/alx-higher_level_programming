#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    real_number = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
            real_number += 1
        except (ValueError, TypeError):
            pass
    print("")
    return real_number

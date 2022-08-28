#!/usr/bin/python3

def no_c(my_string):
    new_my_string = []
    for n in my_string:
        if n != "c" or n != "C":
            new_my_string.append(n)
        else:
            new_my_string.append("[c]")
    return "".join(new_my_string)

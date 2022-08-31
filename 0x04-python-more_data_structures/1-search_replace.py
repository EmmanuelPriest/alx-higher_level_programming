#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for n in range(len(my_list)):
        if my_list[n] == search:
            new_list[n] = replace
    return new_list

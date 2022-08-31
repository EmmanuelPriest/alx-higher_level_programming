#!/usr/bin/python3

def uniq_add(my_list=[]):
    return (set(map(lambda x: x + x for n in range(len(my_list)))))

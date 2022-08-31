#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    a, b = list(set_1.difference(set_2)), list(set_2.difference(set_1))
    od_set = a + b
    return od_set

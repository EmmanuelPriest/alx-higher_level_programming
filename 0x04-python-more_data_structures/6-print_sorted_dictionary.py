#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(n, a_dictionary[n])) for n in sorted(a_dictionary)]

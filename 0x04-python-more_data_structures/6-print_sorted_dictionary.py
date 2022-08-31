#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_dict = dict(sorted(a_dictionary.items(), key=lambda n: n[0].lower()))
    for key, value in sort_dict.items():
        print("{} : {}".format(key, value))

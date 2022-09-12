#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError
    except TypeError:
        print("Exception raised")
        raise

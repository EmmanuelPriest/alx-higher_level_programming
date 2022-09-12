#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        raise NameError("wrong name")
    except NameError:
        print("Exception is raised")

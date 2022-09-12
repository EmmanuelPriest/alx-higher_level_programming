#!/usr/bin/python3

from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)
    except Exception as E:
        print("Exception: {}".format(E), file=sys.stderr)
        return None
    else:
        return func

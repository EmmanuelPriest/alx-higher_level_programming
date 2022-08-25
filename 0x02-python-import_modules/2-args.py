#!/usr/bin/python3
import sys
if __name_ == "__main__":

    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number))
    for n in range(number):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))

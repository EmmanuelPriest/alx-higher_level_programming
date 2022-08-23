#!/usr/bin/python3
def uppercase(str):
    for str in range(65, 91):
        if ord(str) >= 65 and ord(str) <= 90:
            print("{}".format(chr(str)))

#!/usr/bin/python3
def uppercase(str):
    for str in range(97, 123):
        if ord(str) >= 97 and ord(str) <= 122:
            print("{}".format(chr(ord(str) - 32)))

#!/usr/bin/python3
def islower(c):
    for c in range(97, 123):
        if ord(c) >= 'a' and ord(c) < 'z':
            return True
        else:
            return False

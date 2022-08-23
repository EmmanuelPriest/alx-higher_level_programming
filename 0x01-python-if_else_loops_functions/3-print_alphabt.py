#!/usr/bin/python3
for n in range(97, 123):
    if n not in (ord('q'), ord('e')):
        print("{}".format(chr(n)), end="")

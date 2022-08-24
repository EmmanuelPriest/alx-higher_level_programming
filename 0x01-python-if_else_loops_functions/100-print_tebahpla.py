#!/usr/bin/python3
n = 0
for m in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(m - n)), end="")
    n = 32 if n == 0 else 

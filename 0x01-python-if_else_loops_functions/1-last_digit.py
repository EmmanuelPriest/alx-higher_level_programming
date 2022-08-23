#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = number % 10
if number < 0:
    lastD = -lastD
if lastD > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastD))
elif lastD == 0:
    print("Last digit of {} is {} and is 0".format(number, lastD))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastD))

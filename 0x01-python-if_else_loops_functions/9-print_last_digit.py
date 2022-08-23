#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number) % 10
    if (n < 0):
        n *= -1
        print('0' + n)
        return n

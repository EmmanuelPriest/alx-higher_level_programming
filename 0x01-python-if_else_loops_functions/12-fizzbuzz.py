#!/usr/bin/python3
def fizzbuzz():
    for n in range(101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end="")
            continue
        elif n % 3 == 0:
            print("Fizz", end="")
            continue
        elif n % 5 == 0:
            print("Buzz", end="")
            continue
        else:
            print("{} ".format(n), end="")

#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operat = {"+": add, "_": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(operat.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.srgv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b,
                                 operat[sys.argv[2]](a, b)))

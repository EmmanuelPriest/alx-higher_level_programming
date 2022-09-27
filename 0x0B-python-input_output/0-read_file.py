#!/usr/bin/python3

'''Defines a method that reads a text file(UTF8) and print to STDOUT'''


def read_file(filename=""):
    '''Reads a text file and prints to stdout

    Args:
        filename (str): The file to be read

    '''
    with open("filename=my_file_0.txt", encoding="utf-8") as f:
        read_file = f.read()
        print(read_file)

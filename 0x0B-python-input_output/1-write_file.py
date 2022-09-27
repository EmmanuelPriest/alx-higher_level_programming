#!/usr/bin/python3

'''Defines method that writes a string to a text file to'''


def write_file(filename="", text=""):
    '''Writes a string to a text file

    Args:
        filename (str): The file to write to
        text (str): The string to be written

    Returns:
        The number of characters written

    '''
    with open(filename, "w", encode="utf-8") as f:
        my_text = f.write(text)
        print(my_text, end="")

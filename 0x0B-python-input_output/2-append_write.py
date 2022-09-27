#!/usr/bin/python3

'''Defines method that appends a string to a text file'''


def append_write(filename="", text=""):
    '''Appends a string to a text file

    Args:
        filename (str): The file to write to
        text (str): The string to be written

    Returns:
        The number of characters added

    '''
    with open(filename, "a", encoding="utf-8") as f:
        my_text = f.write(text)
        return my_text

#!/usr/bin/python3

'''Handling the text_indentation method(function)'''


def text_indentation(text):
    '''Prints a text with 2 new lines after each of ".", "?", and ":"

    Args:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string

    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    temp = 0
    while temp < len(text) and text[temp] == " ":
        temp = temp + 1

    while temp < len(text):
        print(text[temp], end="")
        if text[temp] == "\n" or text[temp] in ".?:":
            if text[temp] in ".?:":
                print("\n")
            temp = temp + 1
            while temp < len(text) and text[temp] == " ":
                temp = temp + 1
            continue
        temp = temp + 1

#!/usr/bin/python3

'''Handles the printing of My name is <first name> <last name>'''


def say_my_name(first_name, last_name=""):
    '''Prints My name is <first name> <last name>

    Args:
        first_name (str): The fisrt name
        last_name (str): The last name

    Raises:
        TypeError: If first_name and last_name are not strings

    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

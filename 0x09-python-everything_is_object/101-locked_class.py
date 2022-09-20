#!/usr/bin/python3

'''Defining class LockedClass'''


class LockedClass:
    '''

    Preventing the user from dynamically creating new instance attribute
    except if the new instance attribute is first_name

    '''

    __slots__ = ["first_name"]

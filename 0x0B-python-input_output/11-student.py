#!/usr/bin/python3

'''Defines a Student class'''


class Student:
    '''Represent a student'''

    def __init__(self, first_name, last_name, age):
        '''Init method that initialize a new Student

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Dictionary representation of the Student
        If attrs is a list of strings, represents only those attributes
        included in the list

        Args:
            attrs (list): (Optional) The attributes to represent

        '''
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return self.__dict__

    def reload_from_json(self, json):
        '''Method that replaces all attributes of the Student

        Args:
            json (dict): The key/value pairs to replace attributes with

        '''
        for k, v in json.items():
            setattr(self, k, v)

#!/usr/bin/python3

'''Defines the class Base'''
import json
import csv
import turtle


class Base:
    '''Representation of the class Base
     The parent of all the classes in Python project 0x0C*

     Attributes:
        __nb_objects (int): The private class Base attribute

    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializes the Init method of class Base

        Args:
            id (int): The identity of the class Base

        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON serialization of a list of dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            If list_dictionaries is None or empty - the string: "[]"
            Otherwise, the JSON string representation of list_dictionaries

        '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Returns JSON serialization of a list of objects

        Args:
            list_objs (list): A list of instances that inherits Base

        '''
        name_of_file = cls.__name__ + ".json"
        with open(name_of_file, "w", encoding="utf-8") as nof:
            if list_objs is None:
                nof.write("[]")
            else:
                list_of_dicts = [obj.to_dictionary() for obj in list_objs]
                nof.write(Base.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''Returns the deserialization of a list of JSON string

        Args:
            json_string (list): A JSON string representing a list of dicts

        Returns:
            If json_string is None or empty - an empty list
            otherwise, Python list represented by json_string

        '''
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set

        Args:
            **dictionary (dict): key/value pairs of initialized attributes

        '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances from a file of JSON strings
        Reads from `<cls.__name__>.json`

        Returns:
            If the file doesn’t exist - an empty list
            Otherwise, a list of instances from a file of JSON strings

        '''
        name_of_file = str(cls.__name__) + ".json"
        try:
            with open(name_of_file, "r", encoding="utf-8") as nof:
                list_of_dicts = Base.from_json_string(nof.read())
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Returns CSV serialization of a list of objects

        Args:
            list_objs (list):  A list of instances that inherits Base

        '''
        name_of_file = cls.__name__ + ".csv"
        with open(name_of_file, "w", newline="") as nof:
            if list_objs is None or list_objs == []:
                nof.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    rec_instances = ["id", "width", "height", "x", "y"]
                else:
                    sq_instances = ["id", "size", "x", "y"]
                creator = csv.DictWriter(nof, rec_instances=sq_instances)
                for obj in list_objs:
                    creator.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Returns a list of instances from a CSV file
         Reads from `<cls.__name__>.json`

         Returns:
            If the file doesn’t exist - an empty list
            Otherwise, a list of instances from a CSV file

        '''
        name_of_file = cls.__name__ + ".csv"
        try:
            with open(name_of_file, "r", newline="") as nof:
                if cls.__name__ == "Rectangle":
                    rec_instances = ["id", "width", "height", "x", "y"]
                else:
                    sq_instances = ["id", "size", "x", "y"]
                    list_of_dicts = csv.DictReader(nof,
                                                   rec_instances=sq_instances)
                    list_of_dicts = [dict([key, int(value)]
                                     for key, value in d.items())
                                     for d in list_of_dicts]
                    return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Opens a window and draws Rectangles and Squares using turtle module

        Args:
            list_rectangles (list): A list of Rectangle obj to be drawn
            list_squares (list): A list of Square obj to be drawn

        '''
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rectangle in list_rectangle:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for n in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for n in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

#!/usr/bin/python3

"""This module contains the base class of all class
in this project"""

import json
import os
import csv
import turtle


class Base:
    """base class of all Geometric Shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base class initialization

        Args:
            id(int): unique id for each instance of Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries(list): list of objects of class Base
        Return:
            (list): a list of json(str) representation of objects
        """
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
                return
            json_object = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            file.write(json_object)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        x_origin_or_height = 1
        if cls.__name__ == "Square":
            x_origin_or_height = 0

        new_instance = cls(1, x_origin_or_height)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + '.json'
        if not os.path.exists(file_name):
            return []
        with open(file_name, 'r', encoding='utf-8') as file:
            return [cls.create(**obj)
                    for obj in cls.from_json_string(file.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """convert list of objects into csv format"""
        object_dicts = [obj.to_dictionary() for obj in list_objs]
        header = object_dicts[0].keys()
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(object_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """convert csv file into list of class instance"""
        file_name = cls.__name__ + '.csv'
        if not os.path.exists(file_name):
            return []

        list_instance = []
        with open(file_name, 'r', encoding='utf-8') as file:
            keys = Base.__to_list(file.readline())  # get the keys
            for line in file:
                values = [int(val) for val in Base.__to_list(line)]
                obj_dict = dict(zip(keys, values))  # convert to dictionary
                list_instance.append(cls.create(**obj_dict))
        return list_instance

    @staticmethod
    def __to_list(string):
        """convert a csv string into a list of strings"""
        return [value.strip() for value in string.split(',')]

    def draw(list_rectangles, list_squares):
        """draw a shape (child instance of Base) e.g Rectangle, Square"""
        my_turtle = turtle.Turtle()
        turtle.bgcolor("black")
        my_turtle.pencolor("white")
        my_turtle.speed(1)
        my_turtle.pensize(3)
        width = -100

        for shape in list_rectangles + list_squares:
            Base.drawshape(my_turtle, shape, width)
            width = shape.width

        my_turtle.getscreen()._root.mainloop()  # <-- run the Tkinter main loop

    @staticmethod
    def drawshape(screen, shape, prev_width):
        screen.penup()
        screen.setx(prev_width + shape.width)
        screen.sety(prev_width * 2)
        screen.pendown()
        # screen.goto(shape.x, shape.y)
        screen.left(90)
        for i in range(4):
            if i % 2 == 0:
                screen.forward(shape.height)
            else:
                screen.forward(shape.width)
            screen.left(90)

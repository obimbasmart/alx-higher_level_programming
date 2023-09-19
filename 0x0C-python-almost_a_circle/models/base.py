#!/usr/bin/python3

"""This module contains the base class of all class
in this project"""

import json


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

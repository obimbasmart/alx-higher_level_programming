#!/usr/bin/python3

"""This module contains the base class of all class
in this project"""


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

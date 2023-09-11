#!/usr/bin/python3

"""
This module contains Write a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """check if @obj is an instance of
    @a_class (directly or indirectly)
    """
    if type(obj) is a_class:
        return False

    return issubclass(obj.__class__, a_class)

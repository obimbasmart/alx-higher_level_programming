#!/usr/bin/python3

"""this module contains function that adds an
attribute to an object if possible"""


def add_attribute(obj, attr_name, attr_value):
    """add attribute to object

    Args:
        object(object): an instance of an object
        attr_name(string): name of attribute
        attr_value(object): value of attribute
    """
    if obj.__class__.__module__ == "builtins" or hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)

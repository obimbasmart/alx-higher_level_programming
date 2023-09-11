#!/usr/bin/python3

"""module contains function that returns the list of available attributes
and methods of an object:"""


def lookup(obj):
    """returns the list of available method and attributes"""
    return dir(obj)

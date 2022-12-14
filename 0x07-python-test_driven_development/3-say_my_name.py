#!/usr/bin/python3

"""
This module contains function that prints My name is <first name> <last name>

Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings otherwise, raise a TypeError exception
with the message first_name must be a string or last_name must be a string
You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    """function that prints a name given first and last names

    Args:
        first_name(string): first name
        last_name(string): last name
    Return:
        Nothing
    """
    # check if arguments are valid types (string)
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

#!/usr/bin/python3

"""
This module containsfunction that prints a name
"""


def say_my_name(first_name, last_name=""):
    """prints a name given first and last names

    Args:
        first_name(string): first name
        last_name(string): last name
    Return:
        Nothing
    """
    f_name_seperator = l_name_sep = " "

    # check if arguments are valid types (string)
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name == "" and last_name == "":
        return

    if first_name == "":
        f_name_seperator = ""
    if last_name == "":
        l_name_sep = ""

    print("My name is{}{:s}{}{:s}".format(f_name_seperator,
                                          first_name, l_name_sep, last_name))

#!/usr/bin/python3

""" This module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """adds two integers a and b

    Args
        a(int): first int
        b(int): second int
    Return:
        sum(int): a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

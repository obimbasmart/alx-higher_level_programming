#!/usr/bin/python3

""" This module contains a function that adds two integers

Write a function that adds 2 integers.

- Prototype: def add_integer(a, b=98):
- a and b must be integers or floats, otherwise raise a TypeError exception
    with the message a must be an integer or b must be an integer
- a and b must be first casted to integers if they are float
- Returns an integer: the addition of a and b
- You are not allowed to import any module
"""


def add_integer(a, b=98):
    """adds two integers a and b

    Args
        a(int): first int
        b(int): second int
    Return:
        sum(int): sum of a and b
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

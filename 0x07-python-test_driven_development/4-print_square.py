#!/usr/bin/python3

"""
function that prints a square with the character #.

Prototype: def print_square(size):
size is the size length of the square
size must be an integer, otherwise raise a
    TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message
    size must be >= 0
if size is a float and is less than 0, raise a TypeError exception
    with the message size must be an integer
"""


def print_square(size):
    """function that prints a square with the character #.

    Args:
        size(int): the length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    [print("#" * size) for i in range(size)]

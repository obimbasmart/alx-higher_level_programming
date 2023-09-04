"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size(int): the length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    [print("#" * size) for i in range(size)]

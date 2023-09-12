#!/usr/bin/python3

"""
A class Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle
    i.e, a Square is a Rectangle"""

    def __init__(self, size):
        """instantiation of Square object

        Args:
            size(integer): size of square
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)

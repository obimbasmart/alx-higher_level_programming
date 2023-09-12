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
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """print() and str() formats"""
        return "[{}] {}/{}".format(
            self.__class__.__name__, self.__size, self.__size)

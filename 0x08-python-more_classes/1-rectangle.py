#!/usr/bin/python3

"""
 a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """ a class rectangle that defines a rectangle object"""

    def __init__(self, width=0, height=0):
        """initialize object

        Args:
            width(int): the width of the rectangle
            height(int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter"""
        if not isinstance(width, int):  # must be an integer
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter"""
        if not isinstance(height, int):  # must be an integer
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

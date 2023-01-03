#!/usr/bin/python3

"""
 a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
"""


class Rectangle:
    """ a class rectangle that defines a rectangle object"""

    def __init__(self, width=0, height=0):
        """initialize object

        Args:
            width(int): the width of the rectangle
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

    def __WH_is_zero(self):
        """returns True if either with or
        height is zero, other False"""
        return self.__height and self.__width

    def area(self):
        """returns the area of a Rectangle
            rea = length * width
        """
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of a Rectangle
           perimeter = 2 * (height + width)

           if height or width is 0, perimeter = 0
        """
        if not self.__WH_is_zero():
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """informal string representation"""
        if self.__WH_is_zero() == 0:
            return ""
        _str = (("#" * self.__width) + '\n') * self.__height
        _str = _str[:-1]
        return _str

    def __repr__(self):
        """formal string representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

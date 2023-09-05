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
        Rectangle.__validate_property(width, "width")
        self.__width = width

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter"""
        Rectangle.__validate_property(height, "height")
        self.__height = height

    @staticmethod
    def __validate_property(property, property_name):
        if not isinstance(property, int):  # must be an integer
            raise TypeError("{} must be an integer".format(property_name))
        if property < 0:
            raise ValueError("{} must be >= 0".format(property_name))

    def area(self):
        """returns the area of a Rectangle
            area = length * width
        """
        return self.height * self.width

    def perimeter(self):
        """returns the perimeter of a Rectangle
           perimeter = 2 * (height + width)

           if height or width is 0, perimeter = 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

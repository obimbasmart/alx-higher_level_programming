#!/usr/bin/python3

"""
A class Rectangle that inherits from BaseGemometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry
    i.e, a Rectangle is a BaseGeometry"""

    def __init__(self, width, height):
        """instantiation of Rectangle object

        Args:
            width(integer): width of Rectangle
            height(integer): height of Rectangle
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of a Rectangle"""
        return self.__width * self.__height

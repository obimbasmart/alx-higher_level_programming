#!/usr/bin/python3

"""
A class BaseGeometry (based on 7-base_geometry.py).
"""


class BaseGeometry:
    """A base Geometry class"""

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """return area of geometry"""
        raise Exception("area() is not implemented")

#!/usr/bin/python3

""" This module holds a blueprint for a square shape"""


class Square:
    """ a class Square that defines a square
    """

    def __init__(self, size=0):
        """ initialization of object data

        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """ getter for private var: size"""
        return self.__size

    @size.setter
    def size(self, size):
        """ setter func for size var """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ compute the area of a square

        Return:
            int: area of square
        """
        return self.__size ** 2

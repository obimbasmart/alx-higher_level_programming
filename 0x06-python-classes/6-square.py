#!/usr/bin/python3

""" This module holds a blueprint for a square shape"""


class Square:
    """ a class Square that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ initialization of object data

        Args:
            size (int): size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ getter for private var: position"""
        return self.__position

    @position.setter
    def position(self, position):
        """ set position """
        if self.__is_invalid_position(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ compute the area of a square

        Return:
            int: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print('')    # print y origin

        for idx in range(self.__size):
            print(' ' * self.__position[0], end='')    # print origin

            for idy in range(self.__size):
                print("#", end='')
            print()

    def __is_invalid_position(self, position):
        """ check if position is a valid square poistion"""
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not isinstance(position[0], int) or
                not isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
            return (1)

        return (0)

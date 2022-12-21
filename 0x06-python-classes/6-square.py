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
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """ getter for private var: position"""
        return self.__position

    @position.setter
    def position(self, position):
        """ setter func for size position """
        if not isinstance(position, tuple
                          ) or len(position) > 2 or len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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

        for i in range(self.__position[1]):
            print('')    # print y origin

        for idx in range(self.__size):
            print(' ' * self.__position[0], end='')    # print origin

            for idy in range(self.__size):
                print("#", end='')
            print()

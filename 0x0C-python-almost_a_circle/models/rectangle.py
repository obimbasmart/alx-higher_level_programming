#!/usr/bin/python3


""" module implementation of class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base:
    a rectangle is a geometric shape"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of Rectangle object

        Args:
            height(int): height of Rectangle
            width(int): width of Rectangle
            x(int): x coordinate of origin
            y(int): y coordinate of origin
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        Rectangle.__validate(value, "height")
        self.__height = value

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        Rectangle.__validate(value, "width")
        self.__width = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        Rectangle.__validate(value, "x")
        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        Rectangle.__validate(value, "y")
        self.__y = value

    @staticmethod
    def __validate(value, name):
        """validate the rectangle attributes
        Args:
            value(int): value to validate
            name(string): name of attribute
        """
        if not type(value) is int:
            raise TypeError("{:s} must be an integer".format(name))
        if name in "xy" and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))
        if name not in "xy" and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))

    def area(self):
        """return area of rectangle"""
        return self.height * self.width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        [print('') for i in range(self.y)]  # print y origin

        for idx in range(self.height):
            print(' ' * self.x, end='')  # print x origin
            [print("#", end='') for i in range(self.width)]
            print()

    def __str__(self):
        """return string representation of Rectangle instance"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id,
            self.x, self.y,
            self.width, self.height
        )

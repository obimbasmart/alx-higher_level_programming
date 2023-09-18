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

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """update instance attribute"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update instance attribute"""
        if len(args):
            self.__update(*args)
        else:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        class_name = self.__class__.__name__
        attr_names = [name[len(class_name) + 3:] if class_name in name
                      else name for name in self.__dict__.keys()]
        return {key: self.__getattribute__(key) for key in attr_names}

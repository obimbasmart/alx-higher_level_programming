#!/usr/bin/python3

"""class Square that inherits from Rectangle

a Square is a special Rectangle, so it makes sense this class
Square inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle
    A square is a special Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """object instantiation
        Args:
            size(int): size of square
            x(int): x coordinate of origin
            y(int): y coordinate of origin
            id(int): unique object identification
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """update instance attribute"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
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

    def __str__(self):
        """return string representation of Rectangle instance"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id,
            self.x, self.y,
            self.width
        )

    def to_dictionary(self):
        """dictionary representation of Square"""
        attr_names = ["id", "size", "x", "y"]
        return {key: self.__getattribute__(key) for key in attr_names}

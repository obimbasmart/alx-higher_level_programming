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

    def __str__(self):
        """return string representation of Rectangle instance"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id,
            self.x, self.y,
            self.width
        )

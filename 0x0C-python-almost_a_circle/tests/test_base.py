#!/usr/bin/python3


""" Unit tests for a Rectangle Class """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


def setUpModule():
    global shape_1, shape_2, shape_3
    global r1, r2, s1, s2

    shape_1 = Base()
    shape_2 = Base(100)
    shape_3 = Base()

    r1 = Rectangle(10, 4)
    r2 = Rectangle(5, 2, id=99)

    s1 = Square(10, id=101)
    s2 = Square(5, id=102)


class TestBase(unittest.TestCase):
    """Class for testing the Base class of Geometric shapes"""

    def test_id(self):
        self.assertEqual(shape_1.id, 1)
        self.assertEqual(shape_2.id, 100)
        self.assertEqual(shape_3.id, 2)

    def test_to_json_string_rectangle(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        list_rect = [r1, r2]
        self.assertEqual(
            Base.to_json_string([obj.to_dictionary()for obj in list_rect]),
            '[{"width": 10, "height": 4, "x": 0, "y": 0, "id": 3}, {"width": 5, "height": 2, "x": 0, "y": 0, "id": 99}]')

    def test_to_json_string_square(self):
        list_square = [s1, s2]
        self.assertEqual(
            Base.to_json_string([obj.to_dictionary() for obj in list_square]),
            '[{"id": 101, "size": 10, "x": 0, "y": 0}, {"id": 102, "size": 5, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(
            Base.from_json_string('[{"width": 10, "height": 4, "x": 0, "y": 0, "id": 3}]'), [{"width": 10, "height": 4, "x": 0, "y": 0, "id": 3}],)
        self.assertEqual(
            Base.from_json_string('[{"id": 101, "size": 10, "x": 0, "y": 0}, {"id": 102, "size": 5, "x": 0, "y": 0}]'), [{"id": 101, "size": 10, "x": 0, "y": 0}, {"id": 102, "size": 5, "x": 0, "y": 0}])

    def test_create(self):
        obj_dict_rect = r1.to_dictionary()
        obj_dict_sqr = s1.to_dictionary()
        new_r1 = Rectangle.create(**obj_dict_rect)
        new_s1 = Square.create(**obj_dict_sqr)
        self.assertEqual(new_r1.to_dictionary(), r1.to_dictionary())
        self.assertEqual(new_s1.to_dictionary(), s1.to_dictionary())
        self.assertEqual(new_r1 == r1, False)
        self.assertEqual(new_s1 == s1, False)

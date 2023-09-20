#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle


def setUpModule():
    global r1, r2
    r1 = Rectangle(10, 4)
    r2 = Rectangle(5, 2, id=99)


class TestRectangle(unittest.TestCase):

    def setUp(self):
        r1.width = 10
        r1.height = 4
        r1.x = 0
        r1.y = 0

    def test_id(self):
        self.assertEqual(r1.id, 4)
        self.assertEqual(r2.id, 99)

    def test_width(self):
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 5)

        r1.width = 3
        r2.width = 5

        self.assertEqual(r1.width, 3)
        self.assertEqual(r2.width, 5)

        with self.assertRaises(ValueError):
            r1.width = -1
            Rectangle(-22, 100)
            Rectangle(0, 42)

        with self.assertRaises(TypeError):
            r1.width = "4"
            Rectangle("3", 2)

    def test_height(self):
        self.assertEqual(r1.height, 4)
        self.assertEqual(r2.height, 2)

        r1.height = 3
        r2.height = 5

        self.assertEqual(r1.height, 3)
        self.assertEqual(r2.height, 5)

        with self.assertRaises(ValueError):
            r1.height = -1
            Rectangle(8, -3)
            Rectangle(2, "3")

        with self.assertRaises(TypeError):
            r1.width = "4"
            Rectangle("3", 2)

    def test_x_orgin(self):
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 0)

        r1.x = 4
        r2.x = 8

        self.assertEqual(r1.x, 4)
        self.assertEqual(r2.x, 8)

        with self.assertRaises(ValueError):
            r1.x = -1
            Rectangle(4, 2, -2)

        with self.assertRaises(TypeError):
            r1.x = "4"
            Rectangle(4, 2, -7)

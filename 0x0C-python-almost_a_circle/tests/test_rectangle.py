#!/usr/bin/pythoon3

""" Module contains unit test for a Rectangle Object"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(10, 20, 3, 3, 100)

    def tearDown(self):
        del self.r1
        del self.r2

    def test_id(self):
        self.assertEqual(self.r1.id, 4)
        self.assertEqual(self.r2.id, 100)

    def test_width(self):
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r2.width, 10)

        self.r1.width = 3
        self.r2.width = 5

        self.assertEqual(self.r1.width, 3)
        self.assertEqual(self.r2.width, 5)

        with self.assertRaises(ValueError):
            self.r1.width = -1
            Rectangle(-22, 100)
            Rectangle(0, 42)

        with self.assertRaises(TypeError):
            self.r1.width = "4"
            Rectangle("3", 2)

    def test_height(self):
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 20)

        self.r1.height = 3
        self.r2.height = 5

        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r2.height, 5)

        with self.assertRaises(ValueError):
            self.r1.height = -1
            Rectangle(8, -3)
            Rectangle(2, "3")

        with self.assertRaises(TypeError):
            self.r1.width = "4"
            Rectangle("3", 2)

    def test_x_orgin(self):
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 3)

        self.r1.x = 4
        self.r2.x = 8

        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r2.x, 8)

        with self.assertRaises(ValueError):
            self.r1.x = -1
            Rectangle(4, 2, -2)

        with self.assertRaises(TypeError):
            self.r1.x = "4"
            Rectangle(4, 2, -7)

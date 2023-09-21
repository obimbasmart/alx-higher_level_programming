#!/usr/bin/python3

"""
Unit Tests for Square Class
"""

import unittest
from models.square import Square
import io
import unittest.mock


def setUpModule():
    global s1, s2
    s1 = Square(1000)
    s2 = Square(10, 3, id=99)


class TestSquare(unittest.TestCase):

    def setUp(self):
        s1.size = 5
        s1.x = 0
        s1.y = 0
        s1.id = 200

    def test_id(self):
        self.assertEqual(s1.id, 200)
        self.assertEqual(s2.id, 99)

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            Square("3", 4, 9, 44)
            Square(5, "4", 5, 37)
            Square(5, 4, "5", 38)

    def test_value_validation(self):
        with self.assertRaises(ValueError):
            Square(0, 1, 9, 44)
            Square(-4, 4, 9, 44)
            Square(2, 0, 9, 44)
            Square(6, -1, 9, 44)

    def test_size(self):
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)

        s1.size = 3
        s2.size = 5

        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.height, 3)

        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)

        with self.assertRaises(ValueError):
            s1.size = -1
            Square(-22, 100)
            Square(0, 42)

        with self.assertRaises(TypeError):
            s1.width = "4"
            Square("3", 2)

    def test_x_orgin(self):
        self.assertEqual(s1.x, 0)
        self.assertEqual(s2.x, 3)

        s1.x = 4
        s2.x = 8

        self.assertEqual(s1.x, 4)
        self.assertEqual(s2.x, 8)

        with self.assertRaises(ValueError):
            s1.x = -1
            Square(4, 2, -2)

        with self.assertRaises(TypeError):
            s1.x = "4"
            Square(3, "4")
            Square(3, 2, "4")

    def test_area(self):
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 100)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, s1, expected_output, mock_stdout):
        s1.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        self.assert_stdout(s1, '#####\n#####\n#####\n#####\n#####\n')
        self.assert_stdout(Square(3, y=2), "\n\n###\n###\n###\n")
        self.assert_stdout(Square(3, x=2), "  ###\n  ###\n  ###\n")
        self.assert_stdout(Square(2, 2, 2, 2), "\n\n  ##\n  ##\n")

    def test_str(self):
        self.assertEqual(str(s1), '[Square] (200) 0/0 - 5')
        self.assertEqual(str(Square(100, 3, id=44)),
                         '[Square] (44) 3/0 - 100')

    def test_update(self):
        fake_sqr = Square(8)
        attrs = {"size": 7, "x": 0, "y": 4, "id": 9}
        fake_sqr.update(**attrs)
        self.assertEqual(fake_sqr.to_dictionary(), {
                         'size': 7, 'x': 0, 'y': 4, 'id': 9})

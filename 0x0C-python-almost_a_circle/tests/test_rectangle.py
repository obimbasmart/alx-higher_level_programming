#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
import io
import unittest.mock


def setUpModule():
    global r1, r2
    r1 = Rectangle(10, 2)
    r2 = Rectangle(5, 3, id=99)


class TestRectangle(unittest.TestCase):

    def setUp(self):
        r1.width = 10
        r1.height = 2
        r1.x = 0
        r1.y = 0

    def test_id(self):
        self.assertEqual(r1.id, 6)
        self.assertEqual(r2.id, 99)

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("3", 1, 4, 9, 44)
            Rectangle(5, "4", 5, 5, 37)
            Rectangle(5, 4, "5", 5, 38)
            Rectangle(5, 4, 5, "5", 39)

    def test_value_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1, 4, 9, 44)
            Rectangle(-4, 3, 4, 9, 44)
            Rectangle(2, 0, 4, 9, 44)
            Rectangle(6, -1, 4, 9, 44)
            Rectangle(5, 4, -3, 5, 37)
            Rectangle(5, 4, 5, -5, 38)

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
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 3)

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

    def test_area(self):
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 15)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, r1, expected_output, mock_stdout):
        r1.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        self.assert_stdout(r1, '##########\n##########\n')
        self.assert_stdout(Rectangle(3, 3, y=2), "\n\n###\n###\n###\n")
        self.assert_stdout(Rectangle(3, 3, x=2), "  ###\n  ###\n  ###\n")
        self.assert_stdout(Rectangle(3, 3, 2, 2), "\n\n  ###\n  ###\n  ###\n")

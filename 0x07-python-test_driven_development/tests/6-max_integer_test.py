#!/usr/bin/python3
"""
Unittest for max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """my unittest class"""

    def test_valid_args(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5, -3, 400, 99]), 400)

    def test_exceptions(self):
        self.assertRaises(TypeError, max_integer(4))

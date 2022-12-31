#!/usr/bin/python3
"""
Unittest for max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """my unittest class"""

    def test_valid_args(self):
        self.assertEqual(max_integer([]), None)   # empty list
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)  # valid list
        self.assertEqual(max_integer([0]), 0)  # single element
        self.assertEqual(max_integer([-5, -3, 400, 99]), 400)  # -ve & +ve nums

    def test_exceptions(self):
        self.assertRaises(TypeError, max_integer(4))   # invalid arg
        self.assertRaises(TypeError, max_integer("list"))   # invalid arg
        self.assertRaises(ValueError, max_integer([1, 4, 5, "six"]))

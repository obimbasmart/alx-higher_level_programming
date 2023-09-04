#!/usr/bin/python3
"""
Unittest for max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """my unittest class"""

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)   # empty list

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positives(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 2]), 4)  # valid list
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)  # max at end
        self.assertEqual(max_integer([6, 2, 3, 4, 5]), 6)  # max at start
        self.assertEqual(max_integer([1, 2, 10, 4, 5]), 10)  # max at middle

    def test_negatives(self):
        self.assertEqual(max_integer([1, 2, -4, 4, 5]), 5)  # one negative num
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)  # all negative

    def test_valid_types(self):
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, "not a list")

    def test_valid_values(self):
        self.assertRaises(ValueError, max_integer, [3, 4, "not a num", 6])

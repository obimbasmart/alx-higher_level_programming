#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class for testing the Base class of Geometric shapes"""

    def test_id(self):
        shape_1 = Base()
        shape_2 = Base(100)
        shape_3 = Base()

        self.assertEqual(shape_1.id, 1)
        self.assertEqual(shape_2.id, 100)
        self.assertEqual(shape_3.id, 2)

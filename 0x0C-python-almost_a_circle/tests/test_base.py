#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class for testing the Base class of Geometric self.shapes"""

    def setUp(self):
        self.shape_1 = Base()
        self.shape_2 = Base(100)
        self.shape_3 = Base()

    def test_id(self):
        self.assertEqual(self.shape_1.id, 1)
        self.assertEqual(self.shape_2.id, 100)
        self.assertEqual(self.shape_3.id, 2)

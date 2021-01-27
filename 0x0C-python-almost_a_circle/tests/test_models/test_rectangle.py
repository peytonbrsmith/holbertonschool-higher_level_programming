#!/usr/bin/python3
"""Unittest for Rectangle.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRecInit(unittest.TestCase):
    """Test suite for Rectangle() class"""

    # @classmethod
    # def setUpClass(self):
    #     self.b1 = Base()
    #     self.b2 = Base()
    #     self.b3 = Base(12)

    # @classmethod
    # def tearDownClass(self):
    #     del self.b1
    #     del self.b2
    #     del self.b3

    def test_recwithmeasurements(self):
        # Test with rec given width and height
        self.r1 = Rectangle(1, 2)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)

    def test_recwithx(self):
        # Test with rec given width and height and x
        self.r1 = Rectangle(1, 2, 3)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 3)

    def test_recwithy(self):
        # Test with rec given width and height and x and y
        self.r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 4)

if __name__ == '__main__':
    unittest.main()

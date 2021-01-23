#!/usr/bin/python3
"""Unittest for Base.py"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test suite for Base() class"""
    def test_nogivenarg(self):
        # Test ungiven ID, should increment nb_objects and use as ID
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_secondnongivenarg(self):
        # Test 2nd ungiven ID, should increment nb_objects and use as ID
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_givenarg(self):
        # Test given ID, shouldn't increment nb_objects or use it as ID
        b3 = Base(12)
        self.assertEqual(b3.id, 12)


if __name__ == '__main__':
    unittest.main()

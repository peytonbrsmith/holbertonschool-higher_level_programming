#!/usr/bin/python3
"""Unittest for Base.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInit(unittest.TestCase):
    """Test suite for Base() class"""

    @classmethod
    def setUpClass(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(12)

    @classmethod
    def tearDownClass(self):
        del self.b1
        del self.b2
        del self.b3

    def test_nogivenarg(self):
        # Test ungiven ID, should increment nb_objects and use as ID
        self.assertEqual(self.b1.id, 1)

    def test_secondnongivenarg(self):
        # Test 2nd ungiven ID, should increment nb_objects and use as ID
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b1.id, 1)

    def test_givenarg(self):
        # Test given ID, shouldn't increment nb_objects or use it as ID
        self.assertEqual(self.b3.id, 12)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b1.id, 1)


class TestJsonStr(unittest.TestCase):
    """Test suite for Base() classmethod to_json_string"""

    @classmethod
    def setUpClass(self):
        self.r1 = Rectangle(10, 7, 2, 8, 1)
        self.dictionary = self.r1.to_dictionary()
        self.json_dictionary = Base.to_json_string([self.dictionary])
        print(type(self.json_dictionary))
        print(self.json_dictionary)

    @classmethod
    def tearDownClass(self):
        del self.r1
        del self.dictionary
        del self.json_dictionary

    def test_correctusage(self):
        # Test ungiven ID, should increment nb_objects and use as ID
        self.assertIsInstance(self.json_dictionary, str)


if __name__ == '__main__':
    unittest.main()

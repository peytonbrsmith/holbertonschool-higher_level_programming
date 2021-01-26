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
        b1 = Base()
        b2 = Base()
        b3 = Base(12)

    @classmethod
    def tearDownClass(self):
        del b1
        del b2
        del b3

    def test_nogivenarg(self):
        # Test ungiven ID, should increment nb_objects and use as ID
        self.assertEqual(b1.id, 1)

#     def test_secondnongivenarg(self):
#         # Test 2nd ungiven ID, should increment nb_objects and use as ID
#         self.assertEqual(TestBaseInit.b2.id, 2)
#         self.assertEqual(TestBaseInit.b1.id, 1)

#     def test_givenarg(self):
#         # Test given ID, shouldn't increment nb_objects or use it as ID
#         self.assertEqual(TestBaseInit.b3.id, 12)
#         self.assertEqual(TestBaseInit.b2.id, 2)
#         self.assertEqual(TestBaseInit.b1.id, 1)

# class TBtojsonstring(unittest.TestCase):
#     """Test suite for Base() classmethod to_json_string"""

#     @classmethod
#     def setUpClass(self):
#         r1 = Rectangle(10, 7, 2, 8)
#         dictionary = r1.to_dictionary()
#         json_dictionary = Base.to_json_string([dictionary])

#     @classmethod
#     def tearDownClass(self):
#         del self.r1
#         del self.dictionary
#         del self.json_dictionary

#     def test_nogivenarg(self):
#         # Test ungiven ID, should increment nb_objects and use as ID
#         self.assertEqual(TBtojsonstring.r1.id, 1)

#     # def test_secondnongivenarg(self):
#     #     # Test 2nd ungiven ID, should increment nb_objects and use as ID
#     #     self.assertEqual(TBtojsonstring.b2.id, 2)
#     #     self.assertEqual(TBtojsonstring.b1.id, 1)

#     # def test_givenarg(self):
#     #     # Test given ID, shouldn't increment nb_objects or use it as ID
#     #     self.assertEqual(TBtojsonstring.b3.id, 12)
#     #     self.assertEqual(TBtojsonstring.b2.id, 2)
#     #     self.assertEqual(TBtojsonstring.b1.id, 1)




if __name__ == '__main__':
    unittest.main()

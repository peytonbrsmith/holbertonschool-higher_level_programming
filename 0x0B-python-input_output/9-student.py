#!/usr/bin/python3
"""Write a class Student that defines a student by:"""
import json
class_to_json = __import__('8-class_to_json').class_to_json


class Student():
    """
        Student Class

        --------------

        Public instance attributes:
            first_name
            last_name
            age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves class dictionary"""
        return self.__dict__

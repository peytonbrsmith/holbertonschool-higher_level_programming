#!/usr/bin/python3
"""Write a class Student that defines a student by:"""


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
        """inits student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves class dictionary"""
        return self.__dict__

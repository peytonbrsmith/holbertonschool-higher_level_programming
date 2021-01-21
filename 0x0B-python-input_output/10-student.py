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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves class dictionary and specific keys"""
        if attrs:
            new_dict = {}
            for attr in attrs:
                if self.__dict__.get(attr):
                    new_dict[attr] = self.__dict__.get(attr)
            return new_dict
        else:
            return self.__dict__

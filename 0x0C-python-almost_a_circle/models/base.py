#!/usr/bin/python3
"""Write the first class Base:"""


class Base():
    """
    Base Class -

    Class Attributes:
        nb_objects (Private) - # of Base objects

    Public Instance Attributes:
        id = instance ID
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base instance with given ID or nb_objects"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        elif type(id) is not int:
            raise TypeError("id must be an integer")
        else:
            self.id = id

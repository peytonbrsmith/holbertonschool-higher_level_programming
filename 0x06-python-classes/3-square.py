#!/usr/bin/python3
"""This module calculates the area of square given it's size"""


class Square:
    """
    Square Class that holds size

    Attributes:
        __size (integer): the size of the square instance

    """
    def __init__(self, new_size=0):
        """
        Initializes a square of size new_size

        Args:
            new_size: the size for the new square instance

        """
        if isinstance(new_size, int) is True:
            if new_size >= 0:
                self.__size = new_size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the area of the base square"""
        return (self.__size ** 2)

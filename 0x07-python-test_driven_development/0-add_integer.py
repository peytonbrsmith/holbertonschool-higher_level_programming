#!/usr/bin/python3
"""This module includes a single method that adds 2 integers"""


def add_integer(a, b=98):
    """
    ``add_integer`` - returns the sum of its 2 given int/float arguments

    Arguments:
        a - first integer or float, must be given
        b - second integer or float, defaults to 98

    Returns:
        the sum of a and b
    """
    if isinstance(a, float):
        a = int(a)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if isinstance(b, float):
        b = int(b)
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b

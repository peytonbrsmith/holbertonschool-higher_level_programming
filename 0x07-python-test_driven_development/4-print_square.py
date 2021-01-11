#!/usr/bin/python3
"""This module prints a squre with the method print_square"""


def print_square(size):
    """
    print_square - Prints the square size in #s

    Arguments:
    size - the size of the intended square

    Returns: nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size == 0:
            print()
    elif size < 0:
        if type(size) is float:
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("#", end='')
        print()

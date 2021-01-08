#!/usr/bin/python3
"""This module has a single method that prints names"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - says its given names if available

    Arguments:
    first_name - First name of person
    last_name - last name of person

    Return none
    """
    if first_name is "" or type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

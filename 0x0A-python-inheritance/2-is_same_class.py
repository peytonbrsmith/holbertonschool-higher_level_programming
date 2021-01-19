#!/usr/bin/python3
"""Instance Class checker"""


def is_same_class(obj, a_class):
    """
    is_same_class:

    Arguments:
        obj - the obj to check
        a_class - the class type to check against

    Returns: true or false
    """
    if type(obj) is a_class:
        return True
    else:
        return False

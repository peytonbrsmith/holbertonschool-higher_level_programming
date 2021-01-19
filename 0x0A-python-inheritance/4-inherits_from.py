#!/usr/bin/python3
"""Instance inheritance checker"""


def inherits_from(obj, a_class):
    """
    inherits_from:

    Arguments:
        obj - the obj to check
        a_class - the class type to check against

    Returns: true or false
    """
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False

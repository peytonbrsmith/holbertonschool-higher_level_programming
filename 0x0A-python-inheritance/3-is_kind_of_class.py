#!/usr/bin/python3
"""instance class checker and baseclass checker"""


def is_kind_of_class(obj, a_class):
    """instance class checker and baseclass checker"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

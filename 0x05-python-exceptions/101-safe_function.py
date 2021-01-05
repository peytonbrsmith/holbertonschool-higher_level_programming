#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret = fct(*args)
    except Exception as fail:
        sys.stderr.write("Exception: {}\n".format(fail))
        ret = None
    return ret

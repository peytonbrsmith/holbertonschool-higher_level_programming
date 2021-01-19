#!/usr/bin/python3
""""Defines a method to lookup attributes and methods of an object"""


def lookup(obj):
    """"returns a list of attributes and methods of a given object"""
    return list(dir(obj))

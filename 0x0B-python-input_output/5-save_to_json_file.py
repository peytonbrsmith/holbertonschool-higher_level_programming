#!/usr/bin/python3
"""
Write a function that writes an Object to a text file, using a
JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an obj to text file"""
    with open(filename, mode='w+', encoding="utf-8") as myFile:
            return myFile.write(json.dumps(my_obj))

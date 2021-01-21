#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """creates an obj from json"""
    with open(filename, mode='r', encoding="utf-8") as myFile:
            return (json.loads(myFile.read()))

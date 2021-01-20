#!/usr/bin/python3
"""
Write a function that writes an Object to a text file, using a JSON representation:
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_list = []

for obj in sys.argv:
    if obj is not sys.argv[0]:
        new_list.append(obj)
print(load_from_json_file("add_item.json"))
save_to_json_file(new_list, "add_item.json")


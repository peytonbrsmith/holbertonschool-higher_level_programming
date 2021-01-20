#!/usr/bin/python3
"""
Write a function that writes an Object to a text file, using a
JSON representation:
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


new_list = []
old_list = []

for obj in sys.argv:
    if obj is not sys.argv[0]:
        new_list.append(obj)
try:
    old_list = load_from_json_file("add_item.json")
except ValueError:
    pass
if new_list:
    if old_list:
        new_list += old_list
    save_to_json_file(new_list, "add_item.json")

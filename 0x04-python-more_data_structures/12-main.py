#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MMMCMXCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

print("{} = {}".format("NONE", roman_to_int(None)))

print("{} = {}".format(123, roman_to_int(None)))

print("{} = {}".format("I", roman_to_int("I")))

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "M"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "C"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "L"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

print("{} = {}".format("MOM", roman_to_int("MOM")))


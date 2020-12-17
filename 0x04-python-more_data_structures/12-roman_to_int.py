#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        roman_val = 0
        for c in roman_string:
            if c is "X":
                roman_val += 10
            elif c is "V":
                roman_val += 5
            elif c is "I":
                roman_val += 1
            elif c is "L":
                roman_val += 50
            elif c is "C":
                roman_val += 100
            elif c is "D":
                roman_val += 500
            elif c is "M":
                roman_val += 1000
        return (roman_val)
    return (0)

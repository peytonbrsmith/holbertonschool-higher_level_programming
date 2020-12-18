#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_val = 0
    if roman_string is None:
        return (roman_val)
    order = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    numerals = dict([('X', 10), ('V', 5), ('I', 1),
                    ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
    prevnum = 6
    for i in range(len(roman_string) - 1, -1, -1):
        for j in range(0, len(order)):
            if roman_string[i] == order[j]:
                # print("J is {} and Prevnum is {}".format(j, prevnum))
                if j <= prevnum:
                    roman_val += numerals[roman_string[i]]
                else:
                    roman_val -= numerals[roman_string[i]]
                prevnum = j
    return (roman_val)

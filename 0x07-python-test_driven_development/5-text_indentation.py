#!/usr/bin/python3
"""This module adds spaced lines after punctuation"""


def text_indentation(text):
    """Indents text with two newlines after each . ? or :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    addnewline = False
    skip = False
    for char in text:
        skip = False
        if addnewline is True and char is ' ':
            skip = True
        addnewline = False
        if char in list(['.', '?', ':']):
            addnewline = True
        if skip is False:
            print(char, end="")
        if addnewline is True:
            print("\n")

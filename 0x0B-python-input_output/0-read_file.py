#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reads a file, prints to stdout"""
    with open(filename, mode='r') as myFile:
        print(myFile.read(), end="")

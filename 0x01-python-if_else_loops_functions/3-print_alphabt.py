#!/usr/bin/python3
number = 97
while number < 123:
    if number != 101 and number != 113:
        print("{:c}".format(number), end='')
    number = number + 1

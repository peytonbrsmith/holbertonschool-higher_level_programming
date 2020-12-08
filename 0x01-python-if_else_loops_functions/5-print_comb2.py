#!/usr/bin/python3
number = 0
while number < 100:
    if number == 99:
        print("{:02d}".format(number))
    else:
        print("{:02d}".format(number), end=', ')
    number = number + 1

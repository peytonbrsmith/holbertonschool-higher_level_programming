#!/usr/bin/python3
def uppercase(str):
    for i in str:
        number = ord(i)
        if number > 96 and number < 123:
            print("{:c}".format(number - 32), end='')
        else:
            print(i, end='')
    print("")

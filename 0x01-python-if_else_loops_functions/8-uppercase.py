#!/usr/bin/python3
def uppercase(str):
    for i in str:
        lower = ord(i)
        if lower > 96 and lower < 123:
            check = True
        else:
            check = False
        print("{:c}".format((lower - 32) if check else lower), end='')
    print("")

#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        sum = 0
        for num in my_list:
            if num > sum:
                sum = num
        return (sum)
    else:
        return (None)

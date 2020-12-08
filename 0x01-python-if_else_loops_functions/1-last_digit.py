#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
prefix = "Last digit of"
l6suffix = "and is less than 6 and not 0"
g5suffix = "and is greater than 5"

if (number % 10) > 5 and number > 0:
    print(prefix, "{:d} is {:d}".format(number, (number % 10)), g5suffix)
elif (number % 10) == 0:
    print(prefix, "{:d} is {:d} and is 0".format(number, (number % 10)))
elif (number % 10) < 6 and number > 0:
    print(prefix, "{:d} is {:d}".format(number, (number % 10)), l6suffix)
elif number < 0:
    print(prefix, "{:d} is {:d}".format(number, (number % -10)), l6suffix)

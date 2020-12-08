#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i:
            if (i != 8 or j != 9):
                print(i, j, sep='', end=', ')
            else:
                print(i, j, sep='')

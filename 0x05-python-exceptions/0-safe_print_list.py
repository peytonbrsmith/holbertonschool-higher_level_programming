#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    ret = 0

    for idx in my_list:
        if my_list.index(idx) < x:
            try:
                print(idx, end='')
                ret += 1
            except IndexError:
                break
    print("")
    return ret

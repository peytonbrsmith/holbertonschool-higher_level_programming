#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1.copy()
    new_set = new_set.symmetric_difference(set_2)
    return (new_set)

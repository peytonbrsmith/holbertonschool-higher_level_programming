#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    first = True
    best = None
    for key in a_dictionary:
        if first:
            prev = a_dictionary[key]
            best = key
            first = False
        if a_dictionary[key] > prev:
            prev = a_dictionary[key]
            best = key
    return (best)

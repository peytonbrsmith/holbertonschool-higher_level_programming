#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) < 2 and len(tuple_b) != 0:
        tuple_c = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0)
    elif len(tuple_b) > 0:
        tuple_c = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    else:
        return(tuple_a)
    return (tuple_c)

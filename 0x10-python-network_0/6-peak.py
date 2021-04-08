#/usr/bin/python3
"""finds a peak in a list of Integers
"""


def find_peak(list_of_integers):
    """finds peak

    Arguments:
        list_of_integers {[list]} -- [list of integers]

    Returns:
        [int] -- [the peak of the list or None]
    """
    lst = list_of_integers
    peak = None
    for idx in range(0, len(lst)):
        if idx == 0 and len(lst) > 1 and lst[idx + 1] < lst[idx]:
            return (lst[idx])
        elif idx > 0 and lst[idx] > lst[idx - 1] and lst[idx] > lst[idx + 1]:
            return (lst[idx])
        elif lst.count(lst[idx]) == len(lst):
            return (lst[idx])

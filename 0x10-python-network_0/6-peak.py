#!/usr/bin/bash
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    s = int(length / 2)
    lt = list_of_integers

    if s -1 < 0 and s + 1 >= length:
        return lt[s]
    elif s -1 < 0:
        return lt[s] if lt[s] > lt[s + 1] else lt[s + 1]
    elif s + 1 >= length:
        return lt[s] if lt[s] > lt[s - 1] else lt[s - 1]

    if lt[s -1] < lt[s] > lt[s + 1]:
        return lt[s]

    if lt[s + 1] > lt[s _ 1]:
        return find peak(lt[s:])
    return find_peak(lt[:s])

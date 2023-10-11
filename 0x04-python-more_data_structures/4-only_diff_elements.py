#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    mat = []
    if not set_1:
        set1 = []
    if not set_2:
        set_2 = []
    for a in set_1:
        if a not in set_2:
            mat.append(a)
    for b in set_2:
        if b not in set_1:
            mat.append(b)
    return (mat)

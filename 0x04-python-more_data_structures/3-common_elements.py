#!/usr/bin/python3


def common_elements(set_1, set_2):
    mat = []
    if set_1 and set_2:
        for a in set_1:
            if a in set_2:
                mat.append(a)
    return (mat)

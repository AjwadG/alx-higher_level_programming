#!/usr/bin/python3


def search_replace(my_list, search, replace):
    mat = []
    if my_list:
        for a in my_list:
            if a == search:
                mat.append(replace)
            else:
                mat.append(a)
    return (mat)

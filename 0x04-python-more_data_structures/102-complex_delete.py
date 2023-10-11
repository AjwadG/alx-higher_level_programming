#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    a = []
    for key, val in a_dictionary.items():
        if value == val:
            a.append(key)
    for s in a:
        del a_dictionary[s]
    return a_dictionary

#!/usr/bin/python3


def max_integer(my_list=[]):
    Max = None if len(my_list) == 0 else my_list[0]
    for n in my_list:
        Max = n if n > Max else Max
    return Max

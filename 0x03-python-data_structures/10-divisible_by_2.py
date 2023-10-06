#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    div_2 = []
    for n in my_list:
        div_2.append(True if n % 2 == 0 else False)
    return div_2

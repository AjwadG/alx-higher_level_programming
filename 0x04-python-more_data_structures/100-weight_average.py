#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = [(x * y, y) for x, y in my_list]
    suma = 0
    div = 0
    for n in a:
        suma += n[0]
        div += n[1]
    return suma / (div if div != 0 else 1)

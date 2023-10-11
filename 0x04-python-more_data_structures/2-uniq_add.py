#!/usr/bin/python3


def uniq_add(my_list=[]):
    mat = []
    suma = 0
    if my_list:
        for a in my_list:
            if a not in mat:
                mat.append(a)
                suma += a
    return (suma)

#!/usr/bin/python3


def no_c(my_string):
    return ''.join(''.join(my_string.split('c')).split('C'))

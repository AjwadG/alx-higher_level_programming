#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for n in a:
            if (n == a[-1]):
                print("{:d}".format(n), end='')
            else:
                print("{:d}".format(n), end=' ')
        print()

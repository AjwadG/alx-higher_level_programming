#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    mat = []
    if matrix:
        for a in matrix:
            sub = []
            for b in a:
                sub.append(b * b)
            mat.append(sub)
    return (mat)

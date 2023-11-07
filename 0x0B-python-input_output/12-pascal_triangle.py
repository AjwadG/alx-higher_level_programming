#!/usr/bin/python3
"""pascal_triangle funtion module"""


def pascal_triangle(n):
    """represents the Pascal’s triangle in list of lists"""
    if (n <= 0):
        return []
    pas = [[1]]

    for i in range(n - 1):
        tmp = [1]
        for h in range(len(pas[i]) - 1):
            tmp.append(pas[i][h] + pas[i][h + 1])
        tmp.append(1)
        pas.append(tmp)
    return pas

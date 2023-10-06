#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    n = [0, 0]
    for a in range(len(tuple_a[:2])):
        n[a] += tuple_a[a]
    for b in range(len(tuple_b[:2])):
        n[b] += tuple_b[b]
    return (n[0], n[1])

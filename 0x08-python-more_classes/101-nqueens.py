#!/usr/bin/python3
"""challenge of placing N non-attacking queens on an N×N chessboard"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

if not N.isnumeric():
    print("N must be a number")
    sys.exit(1)
N = int(N)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def col(arr, index):
    for a in range(len(arr)):
        if arr[a][index] == 1:
            return False
    return True


def diag(arr, row, col):
    col1 = col - 1
    col2 = col + 1
    for a in reversed(range(row)):
        if len(arr[0]) > col2 and arr[a][col2] == 1:
            return False
        if col1 >= 0 and arr[a][col1] == 1:
            return False
        col1 -= 1
        col2 += 1
    return True


def all(arr, N):
    count = 0
    for a in arr:
        for b in a:
            count += b
    if N == count:
        return True
    else:
        return False


def find(N, start):
    arr = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        if col(arr, start[i]) and diag(arr, i, start[i]):
            arr[i][start[i]] = 1
    if all(arr, N):
        lis = []
        for a in range(N):
            for b in range(N):
                if arr[a][b]:
                    lis.append([a, b])
        print(lis)


def combinations(digits, length, prev=[]):
    """gets all combs"""
    if length == 0:
        return [prev]
    combs = []
    for i in range(len(digits)):
        if digits[i] not in prev:
            prev_extended = prev + [digits[i]]
            combs += combinations(digits, length-1, prev_extended)
    return combs


digits = [i for i in range(N)]
cases = combinations(digits, N)

for a in cases:
    find(N, a)

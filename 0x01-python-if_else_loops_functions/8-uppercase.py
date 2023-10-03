#!/usr/bin/python3
def uppercase(str):
    for c in str:
        a = c
        if (ord(a) >= ord('a') and ord(a) <= ord('z')):
            a = chr(ord(c) - ord('a') + ord('A'))
        print("{}".format(a), end="")
    print("{}".format("\n"), end="")

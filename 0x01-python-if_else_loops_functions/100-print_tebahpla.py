#!/usr/bin/python3
for n in range(26):
    c = chr(25 - n + ord('A'))
    if ((25 - n) % 2 != 0):
        c = chr(ord(c) + ord('a') - ord('A'))
    print('{}'.format(c), end='')

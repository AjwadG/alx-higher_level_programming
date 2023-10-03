#!/usr/bin/python3
for n in range(97, 123):
    if not (n in (113, 101)):
        print('{}'.format(chr(n)), end='')

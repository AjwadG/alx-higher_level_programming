#!/usr/bin/python3
for n in range(100):
    if (n == 89):
        print('{:d}'.format(n))
    elif n < int(n / 10) + n % 10 * 10:
        print('{:02d}'.format(n), end=", ")

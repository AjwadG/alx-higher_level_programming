#!/usr/bin/python3
def fizzbuzz():
    for c in range(1, 101):
        a = ""
        if (c % 3 == 0):
            a += "Fizz"
        if (c % 5 == 0):
            a += "Buzz"
        print("{}".format(a if len(a) else c), end=" ")

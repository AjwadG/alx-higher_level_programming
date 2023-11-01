#!/usr/bin/python3
"""
    add_integer module
    using module doctest
    to check cases
"""


def add_integer(a, b=98):
    """Adds two integers
     Args:
        a: number 1.
        b: number 2 defaults to 98.

    Raises:
        TypeError: if a or b are not numbers

    Returns:
        The sum of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/0-add_integer.txt")

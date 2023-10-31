#!/usr/bin/python3
"""print_square module"""


def print_square(size):
    """printing a square of # of size size.

    Args:
        size: size of the square.

    Raises:
        TypeError: size is not an int.
        ValueError: size is < 0.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((('#' * size + '\n') * size), end="")


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/4-print_square.txt")

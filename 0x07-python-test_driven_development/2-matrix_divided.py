#!/usr/bin/python3
"""
    matrix_divided moudle
    using module doctest
    to check cases
"""


def matrix_divided(matrix, div):
    """Divides matrix by div.
    Args:
        matrix: List of list of numbers
        div: number to fiv with
    Returns:
        list: list of products
    Raises:
        TypeError: matrix is not list of lists of numbers.
        TypeError: If sublists are not all same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for a in matrix:
        if type(a) != list or len(a) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(a) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in a:
            if type(x) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    product = []
    for a in matrix:
        s = []
        for x in a:
            s.append(round(x / div, 2))
        product.append(s)
    return product


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/2-matrix_divided.txt")

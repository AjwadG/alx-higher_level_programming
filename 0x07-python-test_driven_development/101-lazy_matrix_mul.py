#!/usr/bin/python3
"""
    multiply 2 matrixies using numpy module
    using module doctest
    to check cases
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix
    Args:
        m_a: matrix 1
        m_b: matrix 2
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/101-lazy_matrix_mul.txt")

#!/usr/bin/python3
"""
    text_indentation module
    using module doctest
    to check cases
"""


def text_indentation(text):
    """adding 2 newlines after ., ? and :.

    Args:
        text: string

    Raises:
        TypeError: text is not string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    for a in ".?:":
        # print(delim, text.split(delim))
        text = (a + "\n\n").join([line.strip(" ") for line in text.split(a)])

    print(text, end="")


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/5-text_indentation.txt")

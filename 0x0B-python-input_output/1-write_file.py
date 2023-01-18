#!/usr/bin/python3

"""
Return no. of characters of a string
"""


def write_file(filename="", text=""):
    """
    function that writes to a text file
    and return number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

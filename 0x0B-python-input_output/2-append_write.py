#!/usr/bin/python3
"""
append to a file
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a file
    and return the number of characters
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

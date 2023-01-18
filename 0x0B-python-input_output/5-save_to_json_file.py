#!/usr/bin/python3
"""
write an object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w") as f1:
        f1.write(json.dumps(my_obj))

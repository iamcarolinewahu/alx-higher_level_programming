#!/usr/bin/python3
"""
return a python object from json string
"""

import json


def from_json_string(my_str):
    """
    returns python object from a json string
    """

    return json.loads(my_str)

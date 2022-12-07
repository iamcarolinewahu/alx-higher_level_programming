#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        new_dict = a_dictionary
        del new_dict[key]
        return new_dict

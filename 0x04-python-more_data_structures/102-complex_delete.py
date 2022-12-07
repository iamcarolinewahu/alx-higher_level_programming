#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary
    for i, j in new_dict.items():
        if j == value:
            new_dict.pop(i)
    return new_dict

#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dict = dict(a_dictionary)
        for n, m in new_dict.items():
            new_dict[n] = m * 2
        return new_dict

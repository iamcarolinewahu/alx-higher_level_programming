#!/usr/bin/python3

def max_integer(my_list=[]):
    max = 0
    if len(my_list) == 0:
        return None
    for i, num in enumerate(my_list):
        if num > max or i == 0:
            max = num

    return max

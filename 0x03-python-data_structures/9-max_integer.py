#!/usr/bin/python3

def max_integer(my_list=[]):
    max = my_list[0]
    for num in my_list:
        if num > max:
            return max
        if my_list == []:
            return None

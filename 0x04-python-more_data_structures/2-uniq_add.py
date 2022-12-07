#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    set_list = set(my_list)
    unique_list = (list(set_list))
    for num in range(len(unique_list)):
        sum += unique_list[num]
    return sum

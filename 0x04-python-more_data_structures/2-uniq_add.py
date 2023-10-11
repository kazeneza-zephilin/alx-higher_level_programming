#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    new_list = 0
    for i in unique:
        new_list += i
    return (new_list)

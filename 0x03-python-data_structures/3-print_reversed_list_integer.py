#!/usr/bin/python3
# Data structure;list and tuples
def print_reversed_list_integer(my_list=[]):
    """print all integers of a list in reverse order"""
    if isinstance(my_list, list):
        my_list.reverse()
        for idx in my_list:
            print("{:d}".format(idx))

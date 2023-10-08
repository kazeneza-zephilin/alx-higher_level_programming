#!/usr/bin/env python3
def no_c(my_string):
    """Remove all character c and C from a string"""
    new_list = [char for char in my_string if char != 'c' and char != 'C']
    return ("".join(new_list))

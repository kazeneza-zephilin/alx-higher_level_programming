#!/usr/bin/python3
#Data structures,lists and tuples

def element_at(my_list, idx):
    """Retrive an element froma list"""
    if idx < 0 or idx > (len(my_list) -1):
        return None
    return (my_list[idx])

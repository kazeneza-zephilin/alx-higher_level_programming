#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied = dict(map(lambda x: x*2, a_dictionary.values()))
    return (multiplied)

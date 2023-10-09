#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_char = None
    else:
        length = len(sentence)
        first_char = sentence[0]
    ret_tuple = length, first_char
    return (ret_tuple)

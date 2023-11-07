#!/usr/bin/python3
# 1-number_of_lines.py
"""Defines the file read  function."""


def write_file(filename="", text=""):
    """function that write a text to a file"""

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except Exeception as e:
        raise e

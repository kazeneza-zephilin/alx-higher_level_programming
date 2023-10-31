#!/usr/bin/python3
 #5-text_indentation.py
"""define function that print 2 lines after each of the (. ? and :)
    characters
"""
def text_indentation(text):
    """
    function that indentate after each character . ? and :
    Return:
        return indentended string 

    args:
        text(str): the string to be checked

    Raises:
        TypeError: when text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

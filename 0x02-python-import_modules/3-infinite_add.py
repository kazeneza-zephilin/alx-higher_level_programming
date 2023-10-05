#!/usr/bin/python3
import sys
def add_args(arguments):
    total = sum(int(arg) for arg in arguments)
    return total

if __name__ == "__main__":
    arg_list = sys.argv[1:]
    result = add_args(arg_list)
    print(result)
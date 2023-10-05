#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    arg_list = sys.argv
    arg_len = len(arg_list) -1
    #print(arg_list)
    #print(arg_len)
    if arg_len == 1:
        print("1 argument:")
        print("{} : {}".format(arg_len, arg_list[1]))
    elif arg_len == 0:
        print("0 arguments.")
    else:
        for i, arg in enumerate(arg_list[1:], start=1):
            print("{}: {}".format(i, arg))


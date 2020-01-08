#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for num in my_list:
            if i < x:
                print("{}".format(num), end='')
                i += 1
        print()
        return i
    except SyntaxError:
        print()
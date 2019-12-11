#!/usr/bin/python3
def print_last_digit(num):
    if num == 0:
        print('{}'.format(num), end='')
        return(num)
    else:
        last_n = abs(num) % 10
        print('{}'.format(last_n), end='')
        return(last_n)

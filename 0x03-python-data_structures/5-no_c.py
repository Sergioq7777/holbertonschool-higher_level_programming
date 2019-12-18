#!/usr/bin/python3
def no_c(my_string):
    m = ['c','C']
    nw = my_string
    nw = ''.join(j for j in nw if j not in m)
    return (nw)

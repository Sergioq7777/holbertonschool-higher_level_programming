#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    s1 = list(tuple_a)
    s2 = list(tuple_b)
    s1.append(0)
    s1.append(0)
    s2.append(0)
    s2.append(0)
    s3 = [s1[0] + s2[0], s1[1] + s2[1]]
    s3 = s3[:3]
    return(tuple(s3))

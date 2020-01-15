#!/usr/bin/python3


def say_my_name(first_name, last_name=""):

    msg_1 = "first_name must be a string"
    msg_2 = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(msg_1)
    if not isinstance(last_name, str):
        raise TypeError(msg_2)
    print("My name is {:s} {:s}".format(first_name, last_name))

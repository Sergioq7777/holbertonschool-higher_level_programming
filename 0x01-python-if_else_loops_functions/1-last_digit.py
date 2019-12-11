#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of "

if number > 0:
    m = number % 10
else:
    m = number % -10

    if modulo > 5:
        print("{:s} {:d} is {:d} and is greater than 5".format(s, number, m))

    elif modulo == 0:
        print("{:s} {:d} is {:d} and is 0".format(s, number, m))

    elif modulo < 6 and number != 0:
        print("{:s} {:d} is {:d} and is less than 6 and not 0".format(s,number, m))

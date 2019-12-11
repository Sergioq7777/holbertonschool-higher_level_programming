#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    modulo = number % 10
else:
    modulo = number % -10


if modulo > 5:
    print("last digit of {0} is {1} and is grater than 5".format(number, modulo))

elif modulo == 0:
    print("Last digit of {0} is {1} and is 0".format(number, modulo))

elif modulo < 6 and number != 0:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, modulo))

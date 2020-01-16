#!/usr/bin/python3
class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
try:
    dogName = input("Whats is your name :")

    if any(char.isdigit() for char in dogName):

        raise DogNameError

except DogNameError:
    print("Your dogs name can't cointain a number")
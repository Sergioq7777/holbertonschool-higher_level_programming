#!/usr/bin/python3

# Add two values "int/float" and return a addition.
def add_integer(a, b=98): # args = int = add
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

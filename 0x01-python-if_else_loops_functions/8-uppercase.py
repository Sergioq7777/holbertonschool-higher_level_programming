#!/usr/bin/python3
def uppercase(str):
    for upp in str:
        if ord(upp) > 96 and ord(upp) < 123:
            upp = chr((ord(upp) - 32))
        print("{}".format(upp), end='')
    print()

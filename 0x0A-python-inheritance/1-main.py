#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        nl = self[:]
        nl.sort()
        print('{}'.format(nl))

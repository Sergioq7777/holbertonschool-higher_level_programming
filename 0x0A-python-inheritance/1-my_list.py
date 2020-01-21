#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        list_a = self[:]
        list_a.sort()
        print(list_a)
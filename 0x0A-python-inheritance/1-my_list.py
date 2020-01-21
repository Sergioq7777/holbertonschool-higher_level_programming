#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        _list = self[:]
        _list.sort()
        print(_list)

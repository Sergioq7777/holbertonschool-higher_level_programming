#!/usr/bin/python3
""" ADD and Sort elemnts on a list """


class MyList(list):
    def print_sorted(self):
        list_a = self[:]
        list_a.sort()
        print(list_a)

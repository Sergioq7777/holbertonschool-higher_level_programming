#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):

    with open(filename, encoding='utf-8') as file:
        c = 0
        cu = 0

        for line in file:
            cu += 1
        file.seek(0)

        if nb_lines <= 0 or nb_lines >= cu:
            print(file.read(), end='')
            return
        else:
            while c < nb_lines:
                print(file.readline(), end='')
                c += 1

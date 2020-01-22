#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename) as f:
        if nb_lines <= 0 or nb_lines >= len(f.readlines()):
            txt = f.read()
            print(txt, end='')
        else:
            for line in f:
                print(line, end='')
                i += 1
                if i == nb_lines:
                    break

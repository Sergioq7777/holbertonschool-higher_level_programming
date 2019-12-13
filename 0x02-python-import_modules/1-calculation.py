#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as imp
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, imp.add(a, b)))
    print("{} - {} = {}".format(a, b, imp.sub(a, b)))
    print("{} * {} = {}".format(a, b, imp.mul(a, b)))
    print("{} / {} = {}".format(a, b, imp.div(a, b)))

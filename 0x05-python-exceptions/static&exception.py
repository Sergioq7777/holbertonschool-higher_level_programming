#!/usr/bin/python3

class sum:

    @staticmethod
    def getsum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum

def main():
    print("sum :", sum.getsum(1,2,3,4,5))

main()
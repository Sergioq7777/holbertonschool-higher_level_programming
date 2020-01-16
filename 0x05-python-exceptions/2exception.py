#!/usr/bin/python3

num1, num2 = input("Enter 2 values to divide: ").split()

try:
    quotient = int(num1) / int(num2)
    
    print("{}/{} = {}".format(num1, num2, quotient))
    
except ZeroDivisionError:
    print("You can't divede by zero")
else:
    print("You didn't raise an exception")
finally:
    print("I execute no matter what")
    
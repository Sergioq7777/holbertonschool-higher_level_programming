#!/usr/bin/python3
for num in range(90, 64, -1):
    if num % 2 == 0:
        num = num + 32
    else:
        num = num
    print('{}'.format(chr(num)), end='')

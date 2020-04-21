#!/usr/bin/python3
'''X-Request -id'''
import requests
import sys

if __name__ == "__main__":
    var = requests.get(sys.argv[1])
    print(var.headers.get('X-Request-Id'))

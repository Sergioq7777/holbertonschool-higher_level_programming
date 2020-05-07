#!/usr/bin/python3
'''Script that takes in a URL'''
import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
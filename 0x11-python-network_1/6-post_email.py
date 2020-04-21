#!/usr/bin/python3
""" takes Url and email, send an post"""
import requests
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    var = requests.post(sys.argv[1], data)
    print(var.text)

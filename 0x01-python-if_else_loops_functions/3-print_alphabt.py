#!/usr/bin/python3

for char in "abcdefghijklmnopqrstuvwxyz":
    if char in "qe":
        continue

    print("{:s}".format(char), end='')

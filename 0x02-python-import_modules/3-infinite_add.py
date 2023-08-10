#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv)
    integer_sum = 0

    for index in range(1, argv_len):
        integer_sum += int(sys.argv[index])

    print("{:d}".format(integer_sum))

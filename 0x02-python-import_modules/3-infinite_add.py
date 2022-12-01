#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv)
    _sum = 0

    for index in range(1, argv_len):
        int_num = int(sys.argv[index])
        _sum += int_num

    print("{:d}".format(_sum))

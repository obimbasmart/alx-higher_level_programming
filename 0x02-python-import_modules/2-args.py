#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv)

    suffix = ':' if (argv_len - 1) else '.'

    print("{:d} {:s}".format(argv_len - 1,
                             "argument" + suffix if argv_len - 1 == 1
                             else "arguments" + suffix))

    for index in range(1, argv_len):
        print("{:d}: {:s}".format(index, sys.argv[index]))

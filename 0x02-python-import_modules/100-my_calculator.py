#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operators = "+-*/"
    arr_funcs = {'+': add, '-': sub, '*': mul, '/': div}
    arg_list = sys.argv

    if len(arg_list) != 4:
        print("Usage: {} <a> <operator> <b>".format(arg_list[0]))
        sys.exit(1)

    if arg_list[2] in operators:
        func = arr_funcs[arg_list[2]]
        a = int(arg_list[1])
        b = int(arg_list[3])
        print("{:d} {:s} {:d} = {:d}".format(a, arg_list[2], b, func(a, b)))
        sys.exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

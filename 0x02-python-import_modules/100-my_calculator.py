#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] == '+':
        calc = add
    elif argv[2] == '-':
        calc = sub
    elif argv[2] == '*':
        calc = mul
    elif argv[2] == '/':
        calc = div
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)

    result = calc(int(argv[1]), int(argv[3]))
    print("{:d} {:s} {:d} = {:d}".format(int(argv[1]),
        argv[2], int(argv[3]), result))
    exit(0)

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv) - 1
    operators = ["+", "-", "*", "/"]
    if argc != 3:
         print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
         exit(1)
    elif argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] is "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif argv[2] is "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif argv[2] is "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif argv[2] is "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

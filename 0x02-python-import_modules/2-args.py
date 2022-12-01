#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_c = len(argv)
    i = 1
    if argv_c is 0:
        print("{:d} arguments.".format(argv_c))
    elif argv_c is 1:
        print("{:d} argument:".format(argv_c))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_c))
        while i <= argv_c:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1

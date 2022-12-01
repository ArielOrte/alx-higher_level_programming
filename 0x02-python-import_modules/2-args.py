#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv_c = len(argv) - 1
    i = 1
    if argv_c == 0:
        print("{:d} arguments.".format(argv_c))
    elif argv_c == 1:
        print("{:d} argument:".format(argv_c))
        print("{:d}: {:s}".format(i, argv[i]))
    else:
        print("{:d} arguments:".format(argv_c))
        while i <= argv_c:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

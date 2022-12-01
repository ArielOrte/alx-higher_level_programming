#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    i = 0
    result = 0
    while i <= argc:
        result += int(argv[i])
        i += 1
    print("{:d}".format(result))

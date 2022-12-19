#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except ValueError as va:
        sys.stderr.write("Exception: " + str(va) + "\n")
        return False
    except TypeError as va:
        sys.stderr.write("Exception: " + str(va) + "\n")
        return False

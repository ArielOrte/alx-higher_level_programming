#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for index in my_string:
        if index != 'c' and index != 'C':
            new_str += index
    return new_str

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp_list = my_list.copy()
    if 0 <= idx < len(tmp_list):
        tmp_list[idx] = element
    return tmp_list

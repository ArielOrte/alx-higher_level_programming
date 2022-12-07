#!/usr/bin/python3
def uniq_add(my_list=[]):
    answer = 0
    for num in range(len(set(my_list))):
        answer += num
    return answer

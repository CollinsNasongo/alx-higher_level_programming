#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    new_list = list(uniq)
    s = 0

    for i in new_list:
        s = s + i
    return s

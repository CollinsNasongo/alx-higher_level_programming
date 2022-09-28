#!/usr/bin/python3
def common_elements(set_1, set_2):
    lst = list()
    for i in set_1:
        for j in set_2:
            if (i == j):
                lst.append(i)
    set_out = set(lst)
    return set_out

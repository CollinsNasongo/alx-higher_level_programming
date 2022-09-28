#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    lst_1 = [i for i in set_1 if i not in set_2]
    lst_2 = [i for i in set_2 if i not in set_1]
    lst_1.extend(lst_2)
    set_out = set(lst_1)
    return set_out

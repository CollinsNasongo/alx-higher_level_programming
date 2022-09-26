#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list is None):
        return
    elif (len(my_list) == 0):
        return None
    else:
        my_list.sort()
        largest = my_list[len(my_list) - 1]
        return largest

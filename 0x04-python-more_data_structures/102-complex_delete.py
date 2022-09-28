#!/usr/bin/python3
def complex_delete(my_dict, value):
    del_list = []
    for k, v in my_dict.items():
        if k is value:
            del_list.append(k)
    for x in del_list:
        del my_dict[x]
    return(my_dict)

#!/usr/bin/python3
def no_c(my_string):
    i = 0
    ln = len(my_string)
    new_string = ''
    while (i != ln):
        if (my_string[i] == "c" or my_string[i] == "C"):
            i += 1
        else:
            new_string += my_string[i]
            i += 1
    return (new_string)

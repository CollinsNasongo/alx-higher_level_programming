#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_string = ''
    for c in str:
        if (n == i):
            i += 1
            continue
        else:
            new_string = new_string + c
            i += 1
            continue
    return new_string

#!/usr/bin/python3
def uppercase(str):
    new_str = ''
    for c in str:
        val = ord(c)
        if (val >= 65 and val <= 90):
            new_str = new_str + c
        elif (val >= 97 and val <= 122):
            new_char = chr(val - 32)
            new_str = new_str + new_char
        else:
            new_str = new_str + c

    print("{}".format(new_str))

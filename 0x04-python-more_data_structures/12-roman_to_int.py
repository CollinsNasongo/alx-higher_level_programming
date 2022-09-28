#!/usr/bin/python3
def roman_to_int(roman_string):
    if (len(roman_string) == 0 or roman_string is None):
        return 0
    R_str = roman_string.upper()
    ln = len(R_str)
    num = 0
    if (ln == 1):
        num = add_rom(R_str)
    elif (R_str[-1] == "X" and R_str[-2] == "I"):
        new_str = R_str[:-2]
        num = add_rom(new_str) + 9
    elif (R_str[-1] == "V" and R_str[-2] == "I"):
        new_str = R_str[:-2]
        num = add_rom(new_str) + 4
    else:
        num = add_rom(R_str)
    return num


def add_rom(s):
    conv_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    num = 0
    for i in s:
        if i in list(conv_dict):
            num = num + conv_dict[i]
        else:
            return 0
    return num

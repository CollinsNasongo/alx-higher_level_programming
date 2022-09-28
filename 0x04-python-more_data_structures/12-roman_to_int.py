#!/usr/bin/python3
def roman_to_int(roman_string):
    if (len(roman_string) == 0 or roman_string is None):
        return 0

    R_str = roman_string.upper()
    num = 0
    i = 0
    conv_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

    while (i < len(R_str)):
        if (R_str[i] not in list(conv_dict)):
            return 0
        if ((i + 1) != len(R_str)):
            if conv_dict[R_str[i]] < conv_dict[R_str[i + 1]]:
                num = num - conv_dict[R_str[i]]
                i += 1
                continue
            else:
                num = num + conv_dict[R_str[i]]
                i += 1
                continue
        else:
            num = num + conv_dict[R_str[i]]
            i += 1

    return num

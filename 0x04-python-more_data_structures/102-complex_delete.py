#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return None
    value_list = list(a_dictionary.values())

    if value not in value_list:
        return a_dictionary

    for k in a_dictionary.keys():
        if a_dictionary[k] == value:
            del a_dictionary[k]
            return a_dictionary

    return a_dictionary

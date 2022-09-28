#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return None
    sort_values = sorted(a_dictionary.values(), reverse=True)
    sort_dict = dict()

    for i in sort_values:
        for k in a_dictionary.keys():
            if a_dictionary[k] == i:
                sort_dict[k] = a_dictionary[k]
    return list(sort_dict)[0]

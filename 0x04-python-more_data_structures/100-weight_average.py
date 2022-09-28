#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    num = 0
    if len(my_list) == 0:
        return 0
    else:
        for i in range(0, len(my_list)):
            score = score + (my_list[i][0] * my_list[i][1])
            num = num + my_list[i][1]
    return score / num

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_lst = []
    i = 0

    if (list_length <= 0):
        print("Out of range")
        return num_lst
    while (i < list_length):
        try:
            div_lst.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            div_lst.append(0)
        except TypeError:
            print("wrong type")
            div_lst.append(0)
        except IndexError:
            print("out of range")
            div_lst.append(0)
        finally:
            i += 1
    return div_lst

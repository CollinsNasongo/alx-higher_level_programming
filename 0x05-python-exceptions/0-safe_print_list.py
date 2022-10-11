#!/usr/bin/bash
def safe_print_list(my_list=[], x=0):
    counter = 0

    try:
        while(counter < x):
            print(f"{my_list[counter]}", end='')
            counter += 1
    except IndexError:
        print()
        return counter

    print()
    return counter

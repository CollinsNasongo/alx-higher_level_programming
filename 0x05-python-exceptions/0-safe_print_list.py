#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    while True:
        try:
            if counter < x:
                print(my_list[counter], end='')
                counter += 1
            else:
                print()
                return counter
        except IndexError:
            print()
            return counter

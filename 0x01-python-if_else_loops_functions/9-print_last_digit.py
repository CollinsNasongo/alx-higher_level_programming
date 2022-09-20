#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        num = number * -1
        last_num = num % 10
        print(last_num, end='')
        return last_num
    else:
        last_num = number % 10
        print(last_num, end='')
        return last_num

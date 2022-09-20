#!/usr/bin/python3
for i in range(0, 10):
    for x in range(1, 10):
        if (i == x):
            continue
        else:
            print("{}{}, ".format(i, x), end='')
print("\n")

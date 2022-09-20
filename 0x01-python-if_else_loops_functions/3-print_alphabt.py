#!/usr/bin/python3
for a in range(97, 123):
    alpha = chr(a)
    if (alpha == 'q' or alpha == 'e'):
        continue
    else:
        print("{}".format(alpha), end='')

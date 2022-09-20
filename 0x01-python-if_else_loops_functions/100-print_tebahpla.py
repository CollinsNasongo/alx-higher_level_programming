#!/usr/bin/python3
i = 0
asc = 122
while (i < 26):
    i += 1
    print("{}".format(chr(asc)), end='')
    if (asc > 90):
        asc = asc - 33
        continue
    else:
        asc = asc + 31

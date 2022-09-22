#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def add_args():
        arg_list = sys.argv
        ln = len(arg_list)
        result = 0

        for i in range(1, ln):
            result = result + int(arg_list[i])

        print("{:d}".format(result))

    add_args()

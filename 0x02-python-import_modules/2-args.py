#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def get_args():
        arg_list = sys.argv
        ln = len(arg_list) - 1
        num = 1

        if ((ln) == 0):
            print("{:d} arguments.".format(ln))

        elif ((ln) == 1):
            print("{:d} argument:".format(ln))
            print("{:d}: {}".format(num, arg_list[1]))

        else:
            print("{:d} arguments:".format(ln))
            for i in range(1, (ln + 1)):
                print("{:d}: {}".format(num, arg_list[i]))
                i += 1
                num += 1
    get_args()

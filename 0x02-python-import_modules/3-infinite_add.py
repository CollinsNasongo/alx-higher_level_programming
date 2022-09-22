#!/usr/bin/python3
import sys
def add_args():
    """Get number of arguments passed

    Returns:
        prints number of arguments
    """
    arg_list = sys.argv
    ln = len(arg_list)
    result = 0
    for i in range(1, ln):
        result = result + int(arg_list[i])

    print("{:d}".format(result))
add_args()

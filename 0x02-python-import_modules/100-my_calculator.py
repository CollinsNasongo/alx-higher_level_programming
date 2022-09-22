#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arg_list = sys.argv
    ln = len(arg_list)

    if (ln != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = arg_list[2]

    if (op != "+" and op != "-" and op != "*" and op != "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    else:
        a = int(arg_list[1])
        b = int(arg_list[3])

        if op == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

        elif op == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

        elif op == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

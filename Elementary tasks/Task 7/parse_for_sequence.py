import sys

error = "Wrong input. You should enter 1 positive integer."
inp = 'Enter 1 positive integer: '


def get_args_sys():
    args = sys.argv
    return int(args[1]) if len(args) == 2 and args[1].isdigit() else -1


def get_args_inp():
    number = input(inp)
    return int(number) if number.isdigit() else -1

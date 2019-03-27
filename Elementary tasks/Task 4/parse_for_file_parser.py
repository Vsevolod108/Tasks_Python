import sys
from pathlib import Path

error = 'Wrong input. Try again.'
helpMessage = '''You need to input either <path of file> <string for count>,
in this case program will show you amount for strings in file, or
<path of file> <string for search> <string for replace>. In this case program
will replace all previous strings for new.'''
inp = 'Enter params: '


def get_args():
    arguments = sys.argv
    arguments.pop(0)

    def check_args(args):
        if len(args) in (2, 3) and Path(args[0]).is_file() and args[1]:
                return len(args) == 2 or args[2]

    if not check_args(arguments):
        print(helpMessage)
    while not check_args(arguments):
        print(error)
        arguments = input(inp).split()
    return arguments


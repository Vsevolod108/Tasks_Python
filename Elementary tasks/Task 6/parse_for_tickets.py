import sys
from pathlib import Path

error = 'Wrong input. Try again.'
helpMessage = '''You need to enter path for file. File must have a
key-word. It must be "Simple" or "Difficult".'''
do_not_exist = "File don't exist."
inp = 'Enter path: '
simple = 'Simple'
difficult = 'Difficult'


def get_args_from_sys():
    args_from_sys = sys.argv
    keywords_from_sys = []
    if len(args_from_sys) == 2 and Path(args_from_sys[1]).is_file():
        path_from_sys = args_from_sys[1]
        f_from_sys = open(path_from_sys)
        text_from_sys = f_from_sys.read()
        f_from_sys.close()
        if simple in text_from_sys:
            keywords_from_sys.append(simple)
        if difficult in text_from_sys:
            keywords_from_sys.append(difficult)
    return keywords_from_sys


def get_args_from_inp():
    keywords = []
    path = input(inp)
    if Path(path).is_file():
        f = open(path)
        text = f.read()
        f.close()
        if simple in text:
            keywords.append(simple)
        if difficult in text:
            keywords.append(difficult)
    return keywords

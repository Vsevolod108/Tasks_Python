import sys
from pathlib import Path

helpMess = '''You need to enter a path of the file.
This program will count stat of signs.'''
args = sys.argv

path = ''
count = {}


def stat(f_path):
    d = {}
    f = open(f_path)
    for line in f:
        for letter in line:
            d[letter.lower()] = d.get(letter.lower(), 0) + 1
    f.close()
    return d


def ordered(dic):
    lst = []
    for k in dic:
        lst.append((k, dic[k]))
    return sorted(lst, key=lambda x: x[1], reverse=True)


if len(args) == 2:
    path = args[1]
    if Path(path).is_file():
        count = stat(path)
        for item in ordered(count):
            print('\"' + str(item[0]) + '\"' + ": " + str(item[1]) + "\n")
    else:
        print("This file is not Exist.")
        print(helpMess)
else:
    print(helpMess)

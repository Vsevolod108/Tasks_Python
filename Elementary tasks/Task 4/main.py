import parse_for_file_parser as parse

author = '''Dp_158_Python_Vsevolod_Kurchenko
This program will count amount of substring in file or replace
old and new strings, depends on input parameters.'''

print(author)
arguments = parse.get_args()


def read_or_rewrite(args):
    path = args[0]
    str_for_count = args[1]
    f = open(path)
    file_data = f.read()
    f.close()
    if len(args) == 2:
        return str(file_data.count(str_for_count))
    elif len(args) == 3:
        str_for_replace = args[2]
        if str_for_count in file_data:
            s = file_data.replace(str_for_count, str_for_replace)
            f = open(path, "w")
            f.write(s)
            f.close()
            return "String was changed"
        else:
            return "There are no such string."


print(read_or_rewrite(arguments))

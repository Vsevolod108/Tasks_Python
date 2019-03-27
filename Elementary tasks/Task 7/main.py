import parse_for_sequence as parse

author = '''Dp_158_Python_Kurchenko_Vsevolod. Square sequence.
This program display the sequence of numbers, witch square is less then n,
n must positive integer number'''
print(author)


def string_square_sequence(number):
    def sequence():
        a = 0
        while True:
            yield a
            a += 1
    s = ''
    seq = sequence()
    while True:
        value = next(seq)
        if value ** 2 < number:
            s += str(value) + ", "
        else:
            s = s.strip(", ")
            break
    return s


n = parse.get_args_sys()
while n <= 0:
    print(parse.error)
    n = parse.get_args_inp()

print(string_square_sequence(n))

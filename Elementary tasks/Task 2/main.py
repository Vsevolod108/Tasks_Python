import parse_for_letters as parse

author = '''Dp_158_Python_Kurchenko_Vsevolod. Letters.
This program will check is it possible to put one cover
with sides <c> and <d> into another with <a> and <b>.'''
print(author)


def print_answer(a, b, c, d):
    def check_cover():
        if c != d:
            return ((a + b) / (c + d)) ** 2 + ((a - b) / (c - d)) ** 2 >= 2
        else:
            return min(a, b) > c
    return "Yes" if check_cover() else "No"


while True:
    arg = parse.GetArgs()
    side = arg.sides
    answer = print_answer(side['a'], side['b'], side['c'], side['d'])
    print(answer)
    userAnswer = input("Press y/yes if you want to play one more time: ")
    if userAnswer.lower() not in('y', 'yes'):
        break

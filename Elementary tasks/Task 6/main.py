import parse_for_tickets as parse
import time

author = '''Dp_158_Python_Vsevolod_Kurchenko
This program will calculate amount of happy tickets,
using simple or difficult algorithm, depends on the keyword in the file.
You need to input path for a file'''
error = "There is no keyword in the file or file don't exist."
numbers = 10 ** 6
simple = "Simple"
difficult = "Difficult"
print(author)


def count_simple():
    count = 0
    for number in range(numbers):
        n = '{0:0>6}'.format(number)
        left = sum([int(i) for i in n[:3]])
        right = sum([int(i) for i in n[3:]])
        if left == right:
            count += 1
    return count


def count_difficult():
    count = 0
    for number in range(numbers):
        odd = number // 10 ** 5 + number // 10 ** 3 % 10 + number // 10 % 10
        even = number // 10 ** 4 % 10 + number // 10 ** 2 % 10 + number % 10
        if even == odd:
            count += 1
    return count


keywords = parse.get_args_from_sys()
while not keywords:
    print(error)
    keywords = parse.get_args_from_inp()

tickets = {simple: count_simple, difficult: count_difficult}

print("Please, waite, I calculate...\n")

for key in keywords:
    start = time.time()
    print('{} {}'.format(key + ":", tickets[key]()))
    print('{} {:.2f}'.format("Time: ", time.time() - start))

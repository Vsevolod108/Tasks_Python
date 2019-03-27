import argparse

author = "Dp_158_Python_Kurchenko_Vsevolod. Fibonachi."
desc = '''This program display range for fibonacci sequence. 
You should Enter 2 integers through the space'''
helpMess = "You need to enter two integers through the space. Example: 5 12"
error = "You should enter positive integers"

parser = argparse.ArgumentParser(prog=author, usage=desc)
parser.add_argument('a', type=int, help=helpMess)
parser.add_argument('b', type=int, help=helpMess)
args = parser.parse_args()


class FibonacciSeq:
    def __init__(self, n):
        self.n = n
        if n == 0:
            self.seq = [0]
        if n == 1 or n == -1:
            self.seq = [0, 1]
        if abs(n) > 1:
            self.seq = [0, 1]
            for i in range(2, abs(n)+1):
                self.seq.append(self.seq[i-1]+self.seq[i-2])


def print_fibonacci(a, b):
    if a >= 0 and b >= 0:
        return [i for i in FibonacciSeq(max(a, b)).seq if i >= min(a, b)]
    else:
        return error


print(author)
print(desc)
print(print_fibonacci(args.a, args.b))

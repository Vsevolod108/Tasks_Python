import argparse

author = '''Dp_158_Python_Kurchenko_Vsevolod_Fibonacci. 
This program display range for fibonacci sequence. 
You should Enter 2 integers through the space, when you call
the program in cmd. It must be positive
values. If you enter negative number, program will
evaluate it as o. Example: main.py 5 12'''
parser = argparse.ArgumentParser(usage=author)
parser.add_argument('a', type=int)
parser.add_argument('b', type=int)
arguments = parser.parse_args()
first = arguments.a
second = arguments.b
print(author)


class FibonacciSequence:
    def __init__(self, *args):
        if args and len(args) == 1:
            self.min = 0
            try:
                maxim = int(args[0])
                if maxim > 0:
                    self.max = maxim
                else:
                    self.max = 0
            except ValueError:
                self.max = 0
        elif args and len(args) == 2:
            try:
                left = int(args[0])
                right = int(args[1])
                if left < 0:
                    left = 0
                if right < 0:
                    right = 0
                self.min = min(left, right)
                self.max = max(left, right)
            except ValueError:
                self.min = self.max = 0
        else:
            self.min = self.max = 0

    @staticmethod
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    def get_sequence(self):
        s = ''
        seq = self.fibonacci()
        while True:
            value = next(seq)
            if value > self.max:
                break
            if value >= self.min:
                s += str(value) + ", "
        return s


f = FibonacciSequence(first, second)
print(f.get_sequence())

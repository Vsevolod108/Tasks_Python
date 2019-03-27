error = 'You need to input a number more than 0.'
inp = 'Enter side '


class GetArgs:
    sides = {'a': 0.0, 'b': 0.0, 'c': 0.0, 'd': 0.0}

    def __init__(self):
        for i in range(4):
            while True:
                try:
                    value = float(input(inp + chr(97+i) + ": "))
                except ValueError:
                    print(error)
                    continue
                if value > 0.0:
                    self.sides[chr(97+i)] = value
                    break
                else:
                    print(error)

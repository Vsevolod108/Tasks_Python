error = 'Wrong input. Try again.'


class GetArgs:
    triangle = {'name': '', 'a': 0.0, 'b': 0.0, 'c': 0.0}

    def __init__(self):
        while True:
            values = input("Enter triangle: ").split(',')
            if len(values) == 4:
                name = values[0]
                a = values[1]
                b = values[2]
                c = values[3]
                if name and a and b and c:
                    try:
                        a = float(a)
                        b = float(b)
                        c = float(c)
                    except ValueError:
                        print(error)
                        continue
                    if a > 0.0 and b > 0.0 and c > 0.0:
                        self.triangle['name'] = name
                        self.triangle['a'] = a
                        self.triangle['b'] = b
                        self.triangle['c'] = c
                        break
            print(error)

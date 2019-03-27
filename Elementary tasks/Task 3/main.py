import parse_for_triangle as parse

author = '''This program will sort triangles by square and show them to you.
You need to input triangle like this: <name>, <side 1>, <side 2>, <side 3>.
Sides must be numbers more than 0.'''
print(author)


class Triangle:
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def is_exist(self):
        a = self.a
        b = self.b
        c = self.c
        if a > 0.0 and b > 0.0 and c > 0.0:
            return a + b > c and a + c > b and b + c > a

    def square(self):
        if self.is_exist():
            a = self.a
            b = self.b
            c = self.c
            p = (a + b + c)/2
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5
        else:
            return -1


def game():
    triangles = []
    while True:
        values = parse.GetArgs()
        name = values.triangle['name']
        a = values.triangle['a']
        b = values.triangle['b']
        c = values.triangle['c']
        triangle = Triangle(name, a, b, c)
        if triangle.is_exist():
            triangles.append(triangle)
        else:
            print("Triangle don't exist.")
            continue
        user_answer = input("Press y/yes, if you want to add one more: ")
        if user_answer.lower() not in ("y", "yes"):
            break
    return sorted(triangles, key=lambda x: x.square())


list_of_triangles = game()
for index, item in enumerate(list_of_triangles):
    print('{}. [{}]: {:.2f} cm'.format(index+1, item.name, item.square()))

import argparse

author = '''Dp_158_Python_Vsevolod_Kutchenko_Numbers_in_words.
This program will print numbers in words. You need to input positive integer'''

parser = argparse.ArgumentParser(usage=author)
parser.add_argument('num', type=int)
args = parser.parse_args()
num = args.num


class Numbers:
    def __init__(self, number):
        self.number = int(number)

    numbers = {
        0: "",
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        10: "десять",
        11: "одиннадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семнадцать",
        18: "восемнадцать",
        19: "девятнадцать",
        20: "двадцать",
        30: "тридцать",
        40: "сорок",
        50: "пятьдесят",
        60: "шестьдесят",
        70: "семьдесят",
        80: "восемьдесят",
        90: "девяносто",
        100: "сто",
        200: "двести",
        300: "триста",
        400: "четыреста",
        500: "пятьсот",
        600: "шестьсот",
        700: "семьсот",
        800: "восемьсот",
        900: "девятьсот",
    }

    big_numbers = {
        0: "",
        1: "ми",
        2: "миллиард",
        3: "три",
        4: "квадри",
        5: "квинти",
        6: "сексти",
        7: "септи",
        8: "окти",
        9: "нони",
        10: "деци",
        11: "ундеци",
        12: "додеци",
        13: "тредеци",
        14: "кваттуордеци",
        15: "квиндеци",
        16: "сексдеци",
        17: "септемдеци",
        18: "октодеци",
        19: "новемдеци",
        20: "вигинти"
    }

    def class_units(self, numb):
        s = self.numbers[numb // 100 * 100] + " "
        n = numb % 100
        if n in range(10, 20):
            s += self.numbers[n]
        else:
            s += self.numbers[n // 10 * 10] + " " + self.numbers[n % 10]
        return s

    def class_thousands(self, numb):
        n = numb // 1000
        if n == 0:
            return ''
        else:
            s = self.class_units(n)
            n %= 100
            if n in (11, 12):
                s += " тысяч"
            elif n % 10 == 1:
                s = s[::-1].replace('нидо', 'андо', 1)[::-1] + " тысяча"
            elif n % 10 == 2:
                s = s[::-1].replace('авд', 'евд', 1)[::-1] + " тысячи"
            elif n % 10 in range(3, 5):
                s += " " + "тысячи"
            else:
                s += " " + "тысяч"
            return s

    def class_big(self, degree):
        shift = 3 + 3*degree
        length = len(str(self.number))
        n = int(str(self.number)[:(length-shift)][::-1][:3][::-1])
        if n == 0:
            return ''
        else:
            s = self.class_units(n)
            if degree == 2:
                s += " миллиард"
            else:
                s += ' ' + self.big_numbers[degree] + 'ллион'
            n %= 100
            if n in range(10, 15):
                s += "ов"
            elif n % 10 in range(2, 5):
                s += "а"
            elif n % 10 in range(5, 10):
                s += "ов"
            return s

    def numbers_in_words(self):
        number = str(self.number)
        words = []
        units = int(number[::-1][:3][::-1])
        thous = int(number[::-1][:6][::-1])
        words.append(self.class_units(units))
        words.append(self.class_thousands(thous))
        length = len(number)
        i = 6
        while i < length:
            i += 3
            degree = i // 3 - 2
            words.append(self.class_big(degree))
        s = ' '.join((' '.join(words[::-1])).split())
        return s if self.number != 0 else 'ноль'


print(author)
if num >= 0:
    inst = Numbers(num)
    print(inst.numbers_in_words())
else:
    print("You should enter positive number.")

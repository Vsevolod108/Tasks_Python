import sys

error = 'Wrong input. It must be a positive integer.'
helpMessage = 'You need to input height and width'


class GetArgs:
    height = ''
    width = ''

    def __init__(self):
        args = sys.argv
        if len(args) == 3:
            if args[1].isdigit() and args[2].isdigit():
                if int(args[1]) > 0 and int(args[2]) > 0:
                    self.height = int(args[1])
                    self.width = int(args[2])
        if not (self.height and self.width):
            print(helpMessage)
            self.get_from_input()

    def get_from_input(self):
        while True:
            height = input('Enter height: ')
            if height.isdigit() and int(height) > 0:
                self.height = int(height)
                break
            else:
                print(error)
        while True:
            width = input('Enter width: ')
            if width.isdigit() and int(width) > 0:
                self.width = int(width)
                break
            else:
                print(error)

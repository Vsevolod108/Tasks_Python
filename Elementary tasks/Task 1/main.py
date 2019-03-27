import parse_for_chess_board as parse

author = '''Dp_158_Python_Vsevolod_Kurchenko_Chess_Board. 
This program will print a chessBoard.'''

print(author)
parser = parse.GetArgs()
height = parser.height
width = parser.width


class ChessBoard:
    def __init__(self, h, w):
            self.h = h
            self.w = w

    def print(self):
        return '\n'.join([('* ' * self.w)[::(-1)**i] for i in range(self.h)])


print(ChessBoard(height, width).print())

# This class is responcible for storing all the info about the current state of a chess game. 
#It will also be responcible for determining the valid moves at the current state. It will also keep a move log.

class Gamestate():
    def __init__(self):
        #board is an 8 x 8 2d list, each element of the list has 2 
        # character, the first character represents the colour of the piece,
        #'b' or 'w', and the second letter represenst the piece i.e 'R' = 'Rook' etc.
        #the -- represents and empty space.
        self.board =[
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.whiteToMove = True
        self.moving = []
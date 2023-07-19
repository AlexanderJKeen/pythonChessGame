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
        self.moveRecording = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        # this will record all move made.
        self.moveRecording.append(move) 
        #this will allow players to switch turns
        self.whiteToMove = not self.whiteToMove


class Move():
    #I want to map the board to match a real chess board and so I am mapping the ranks of chess board to row and the columns to files.
    # Adding a key e.g. desiered key equalling current value key:value

    ranks = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}

    rowsToRanks = {v:k for k, v in ranks.items()}
    files = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h":7}

    colsToFiles = {v:k for k, v in files.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow   = startSq[0]
        self.startCol   = startSq[1]
        self.endRow     = endSq[0]
        self.endCol     = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceTaken = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankAndFile(self.startRow, self.startCol) + self.getRankAndFile(self.endRow, self.endCol)


    def getRankAndFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]

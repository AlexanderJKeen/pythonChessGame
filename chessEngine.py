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

        self.moveFunctions = {"P": self.getPawnMoves, "R": self.getRookMoves, "N": self.getKnightMoves, "B": self.getBishopMoves, "Q": self.getQueenMoves, "K": self.getKingMoves}

        self.whiteToMove = True
        self.moveRecording = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        # this will record all move made.
        self.moveRecording.append(move) 
        #this will allow players to switch turns
        self.whiteToMove = not self.whiteToMove

    # I want the ability to undo a move that may have been made by mistake.

    def undoMove(self):
        #first I want to check if there is a move to undo
        if len(self.moveRecording) != 0:
            #pop() will remove the last move recorded in the moveRecording array.
            move = self.moveRecording.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            #if an opponent piece was taken during this move I must be able to return it back on the board.
            self.board[move.endRow][move.endCol] = move.pieceTaken
            # The turn will then be switched back 
            self.whiteToMove = not self.whiteToMove

    def getValidMoves(self):
        return self.getAllPossibleMoves()
                
    def getAllPossibleMoves(self):
        moves = []
        # This could have an 8 passed through considering I know the board has a length of 8 but I am trying to cut out magic numbers where I can.
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                #This will check the first character of a given space on the board and it will either be "w" for white, "b" for black or "-" for empty. 
                turn = self.board[row][col][0]
                if(turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    # by using the moveFunction dictionary I was able to reduce the amount of code I would need if I used an if statement to select each pieces move function.
                    self.moveFunctions[piece](row, col, moves)
        return moves
                        
    def getPawnMoves(self, row, col, moves):
        if self.whiteToMove:
            #if the pawn moves one square forward.
            if self.board[row-1][col] == "--":
                moves.append(Move((row, col), (row-1, col), self.board))
                #if the pawn moves two spaces forward
                if row == 6 and self.board[row-2][col] == "--":
                    moves.append(Move((row, col),(row - 2, col), self.board))
            # take pieces to the left
            if col-1 >= 0:
                if self.board[row-1][col-1][0] == "b":
                    moves.append(Move((row, col), (row-1, col-1), self.board))
            # take pieces to the right
            if col+1 <= 7:
                if self.board[row-1][col+1][0] == "b":
                    moves.append(Move((row, col), (row-1, col+1), self.board))
        # this will be the black moves
        else:
            #if the pawn moves one square forward.
            if self.board[row + 1][col] == "--":
                moves.append(Move((row, col), (row + 1, col), self.board))
                #if the pawn moves two spaces forward
                if row == 1 and self.board[row + 2][col] == "--":
                    moves.append(Move((row, col),(row + 2, col), self.board))
            # take pieces to the left
            if col - 1 >= 0:
                if self.board[row + 1][col - 1][0] == "w":
                    moves.append(Move((row, col), (row + 1, col - 1), self.board))
            # take pieces to the right
            if col + 1 <= 7:
                if self.board[row + 1][col + 1][0] == "w":
                    moves.append(Move((row, col), (row + 1, col + 1), self.board))



    def getRookMoves(self, row, col, moves):
        directions = ((-1, 0),(0, -1),(1, 0),(0, 1))
        # python turnery statement
        enemyColour = "b" if self.whiteToMove else "w"

        for d in directions:
            for i in range(1,8):
                endRow = row + d[0] * i
                endCol = col + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColour:
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    # if its a friendly piece
                    else:
                        break
                else:
                    break
    
    def getKnightMoves(self, row, col, moves):
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        allyColour = "w" if self.whiteToMove else "b"
        for n in knightMoves:
            endRow = row + n[0]
            endCol = col + n[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8 :
                endPiece = self.board[endRow][endCol] 
                if endPiece[0] != allyColour:
                    moves.append(Move((row, col), (endRow, endCol), self.board))


    def getBishopMoves(self, row, col, moves):
        directions = ((-1, -1),(-1, 1),(1, -1),(1, 1))
        # python turnery statement
        enemyColour = "b" if self.whiteToMove else "w"

        for d in directions:
            for i in range(1,8):
                endRow = row + d[0] * i
                endCol = col + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColour:
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    # if its a friendly piece
                    else:
                        break
                else:
                    break

# AS the queen has the unique movement of both a rook and a bishop it has no unique moves of its own it is far simpler to use the methods I have already created.
# Abstraction.
    def getQueenMoves(self, row, col, moves):
        self.getBishopMoves(row, col, moves)
        self.getRookMoves(row, col, moves)


    def getKingMoves(self, row, col, moves):
        kingMoves = ((-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1))
        allyColour = "w" if self.whiteToMove else "b"
        for i in range(8):
            endRow = row + kingMoves[i][0]
            endCol = row + kingMoves[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColour:
                    moves.append(Move((row, col), (endRow, endCol), self.board))




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
        # This will give each move a unique ID acting as a hash function creating a 4 digit number displaying each number .
        self.moveId     = self.startCol * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

# overriding the equals method. As python does know how to calculate what equals is. 
# The moves generated are the same values they are not the same objects as one was generated by a mouse and the other is stored in the move = [] in getAllPossibleMoves method
# I need to generate an Id for both the moves and stored moves so that the equals can see those two objects as equals.
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId


    def getChessNotation(self):
        return self.getRankAndFile(self.startRow, self.startCol) + self.getRankAndFile(self.endRow, self.endCol)


    def getRankAndFile(self, row, col):
        return self.colsToFiles[col] + self.rowsToRanks[row]

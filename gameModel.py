class GameModel:
    def __init__(self):
        self.DIMENSION = 8
        #board is an 8 x 8 2d list, each element of the list has 2 
        # character, the first character represents the colour of the piece,
        #'b' or 'w', and the second letter represenst the piece i.e 'R' = 'Rook' etc.
        #the -- represents and empty space.
        self.board =[
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]

        self.moveFunctions = {
            'P': self.getPawnMoves, 
            'R': self.getRookMoves, 
            'N': self.getKnightMoves, 
            'B': self.getBishopMoves, 
            'Q': self.getQueenMoves, 
            'K': self.getKingMoves
        }
        
        self.whiteToMove = True
        self.moveRecording = []
        self.whiteKingLocation = (7, 4)
        self.blackKingLocation = (0, 4)
        self.checkMate = False
        self.staleMate = False
    
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        # this will record all move made.
        self.moveRecording.append(move) 
        #this will allow players to switch turns
        self.whiteToMove = not self.whiteToMove
        # This if will now allow the kings location to be updated and monitored by the application.
        if move.pieceMoved == 'wK':
            self.whiteKingLocation = (move.endRow, move.endCol)
        elif move.pieceMoved == 'bK':
            self.blackKingLocation = (move.endRow, move.endCol)

        # promoting a pawn
        if move.pawnPromotion:
            # This will retrieve the colour of the piece i.e 'b'
            self.board[move.endRow][move.endCol] = move.pieceMoved[0] + 'Q'

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
            # This will now undo the Kings location to match the players UI
            if move.pieceMoved == 'wK':
                self.whiteKingLocation = (move.startRow, move.startCol)
            elif move.pieceMoved == 'bK':
                self.blackKingLocation = (move.startRow, move.startCol)            


    def getValidMoves(self):
        # Generate all moves
        moves = self.getAllPossibleMoves()
        #for each of those moves make a move
        #going back through the list allows the list to be 
        #far more reliable as when an item is removed from the list the ordinal number shift wont effect the next iteration through the list.
        for i in range(len(moves)-1, -1, -1):
            self.makeMove(moves[i])
        #generate all opponents moves
        #for each of your opponents moves, see if they attack your king
        # As the makeMove function completes by switching the turns of the player I must switch the turns once again or the inCheck function
        # will check if the person who just moved is in check not the opponent.
            self.whiteToMove = not self.whiteToMove
            if self.inCheck():
            #cannot attack the king 
                moves.remove(moves[i])
            self.whiteToMove = not self.whiteToMove
            self.undoMove()
        if len(moves) == 0:
            if self.inCheck():
                self.checkMate = True
            else:
                self.staleMate = True      
        return moves
    
    def movePiece(self, start_square, end_square):
        start_row, start_col = start_square
        end_row, end_col = end_square
        # Get the piece at the starting square
        piece = self.board[start_row][start_col]
        # If there is no piece at the starting square, return None (no piece to move)
        if piece == "--":
            return None
        # Check if the piece belongs to the current player's color
        if (self.whiteToMove and piece[0] != 'w') or (not self.whiteToMove and piece[0] != 'b'):
            return None
        # Create a Move object to represent the intended move
        move = Move(start_square, end_square, self.board)
        # Get the list of valid moves for the current game state
        moves = self.getValidMoves()
        # If the move is in the list of valid moves, return the Move object representing the move
        if move in moves:
            return move
        # If the move is not valid, return None
        return None
    
    def isValidSquare(self, row, col):
        return 0 <= row < self.DIMENSION and 0 <= col < self.DIMENSION
    
    def inCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])
        
    def squareUnderAttack(self, row, col):
        # Temporarily switch the current player's turn to the opponent's turn
        self.whiteToMove = not self.whiteToMove
        # Generate all possible moves for the opponent's turn
        opponentsMoves = self.getAllPossibleMoves()
        # Switch the player's turn back to the original state
        self.whiteToMove = not self.whiteToMove
        # Check if any of the opponent's moves target the specified square
        for move in opponentsMoves:
            if move.endRow == row and move.endCol == col:
                # The square is under attack
                return True
        # If none of the opponent's moves target the square, it is safe
        return False
        
                
    def getAllPossibleMoves(self):
        moves = []
        # This could have an 8 passed through considering I know the board has a length of 8 but I am trying to cut out magic numbers where I can.
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                #This will check the first character of a given space on the board and it will either be 'w' for white, 'b' for black or '-' for empty. 
                turn = self.board[row][col][0]
                if(turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    # by using the moveFunction dictionary I was able to reduce the amount of code I would need if I used an if statement to select each pieces move function.
                    self.moveFunctions[piece](row, col, moves)
        return moves
                        
    def getPawnMoves(self, row, col, move):
        if self.whiteToMove:
            #if the pawn moves one square forward.
            if self.board[row - 1][col] == '--':
                move.append(Move((row, col), (row-1, col), self.board))
                #if the pawn moves two spaces forward
                if row == 6 and self.board[row-2][col] == '--':
                    move.append(Move((row, col),(row - 2, col), self.board))
            # take pieces to the left
            if col-1 >= 0:
                if self.board[row - 1][col - 1][0] == 'b':
                    move.append(Move((row, col), (row-1, col-1), self.board))
            # take pieces to the right
            if col+1 <= 7:
                if self.board[row - 1][col + 1][0] == 'b':
                    move.append(Move((row, col), (row-1, col+1), self.board))
        else:
            #if the pawn moves one square forward.
            if self.board[row + 1][col] == '--':
                move.append(Move((row, col), (row + 1, col), self.board))
                #if the pawn moves two spaces forward
                if row == 1 and self.board[row + 2][col] == '--':
                    move.append(Move((row, col),(row + 2, col), self.board))
            # take pieces to the left
            if col - 1 >= 0:
                if self.board[row + 1][col - 1][0] == 'w':
                    move.append(Move((row, col), (row + 1, col - 1), self.board))
            # take pieces to the right
            if col + 1 <= 7:
                if self.board[row + 1][col + 1][0] == 'w':
                    move.append(Move((row, col), (row + 1, col + 1), self.board))

    def getRookMoves(self, row, col, move):
        directions = ((-1, 0),(0, -1),(1, 0),(0, 1))
        # python turnery statement
        enemyColour = 'b' if self.whiteToMove else 'w'

        for d in directions:
            for i in range(1,8):
                endRow = row + d[0] * i
                endCol = col + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '--':
                        move.append(Move((row, col), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColour:
                        move.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    # if its a friendly piece
                    else:
                        break
                else:
                    break
    
    def getKnightMoves(self, row, col, move):
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        allyColour = 'w' if self.whiteToMove else 'b'
        for n in knightMoves:
            endRow = row + n[0]
            endCol = col + n[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8 :
                endPiece = self.board[endRow][endCol] 
                if endPiece[0] != allyColour:
                    move.append(Move((row, col), (endRow, endCol), self.board))


    def getBishopMoves(self, row, col, move):
        directions = ((-1, -1),(-1, 1),(1, -1),(1, 1))
        # python turnery statement
        enemyColour = 'b' if self.whiteToMove else 'w'

        for d in directions:
            for i in range(1,8):
                endRow = row + d[0] * i
                endCol = col + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '--':
                        move.append(Move((row, col), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColour:
                        move.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    # if its a friendly piece
                    else:
                        break
                else:
                    break

# AS the queen has the unique movement of both a rook and a bishop it has no unique moves of its own it is far simpler to use the methods I have already created.
# Abstraction.
    def getQueenMoves(self, row, col, move):
        self.getBishopMoves(row, col, move)
        self.getRookMoves(row, col, move)


    def getKingMoves(self, row, col, move):
        kingMoves = ((-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1))
        allyColour = 'w' if self.whiteToMove else 'b'
        for i in range(8):
            endRow = row + kingMoves[i][0]
            endCol = col + kingMoves[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColour:
                    move.append(Move((row, col), (endRow, endCol), self.board))

    
class Move():
    #I want to map the board to match a real chess board and so I am mapping the ranks of chess board to row and the columns to files.
    # Adding a key e.g. desiered key equalling current value key:value

    ranks = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

    rowsToRanks = {v:k for k, v in ranks.items()}
    files = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h':7}

    colsToFiles = {v:k for k, v in files.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow   = startSq[0]
        self.startCol   = startSq[1]
        self.endRow     = endSq[0]
        self.endCol     = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceTaken = board[self.endRow][self.endCol]
        # pawn promotion section
        self.pawnPromotion = (self.pieceMoved == 'wP' and self.endRow == 0) or (self.pieceMoved == 'bP' and self.endRow == 7)
        # This will give each move a unique ID acting as a hash function creating a 4 digit number displaying each number .
        self.moveId = self.startCol * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

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

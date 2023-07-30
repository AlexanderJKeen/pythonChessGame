# chessView.py
import pygame as p

class GameView:
    # Initializes the GameView object with default settings and properties.
    def __init__(self):
        self.WIDTH = self.HEIGHT = 900
        self.DIMENSION = 8
        self.SQ_SIZE = self.HEIGHT // self.DIMENSION
        self.MAX_FPS = 15
        self.IMAGES = {}
        self.screen = None
        self.clock = None

    def loadImages(self):
        # Loads and scales chess piece images from the 'assets' folder.
        pieces = ["wP", "bP", "wR", "bR", "wB", "bB", "wN", "bN", "wQ", "bQ", "wK", "bK"]
        for piece in pieces:
            self.IMAGES[piece] = p.transform.scale(p.image.load("assets/" + piece + ".png"), (self.SQ_SIZE, self.SQ_SIZE))

    def initialize(self):
        # Initializes the Pygame library, sets the screen and clock, and loads chess piece images.
        p.init()
        self.screen = p.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = p.time.Clock()
        self.screen.fill(p.Color("white"))
        self.loadImages()

    def drawBoard(self):
        # Draws the chessboard with alternating light and dark squares.
        colours = [p.Color("white"), p.Color("light gray")]
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                colour = colours[((row + col) % 2)]
                p.draw.rect(self.screen, colour, p.Rect(col * self.SQ_SIZE, row * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def highlightSquare(self, screen, gamesState, validMoves, sqSelected, board):
        # Highlights the selected square and available moves on the chessboard.
        if sqSelected != ():
            row, col = sqSelected
            # sqSelected is a piece that can be moved
            if board[row][col][0] == ('w' if gamesState.whiteToMove else 'b'):
                s = p.Surface((self.SQ_SIZE, self.SQ_SIZE))
                #transparency value
                s.set_alpha(150)
                if board[row][col][0] == 'w':
                    s.fill(p.Color('blue'))
                elif gamesState.board[row][col][0] == 'b':
                    s.fill(p.Color('yellow'))
                screen.blit(s, (col*self.SQ_SIZE, row*self.SQ_SIZE))
                # highlight moves from that square
                if board[row][col][0] == 'w':
                    s.fill(p.Color('yellow'))
                elif board[row][col][0] == 'b':
                    s.fill(p.Color('black'))
                for move in validMoves:
                    if move.startRow == row and move.startCol == col:
                        screen.blit(s, (move.endCol*self.SQ_SIZE, move.endRow * self.SQ_SIZE))

    def drawPieces(self, board):
        # The 2D array representing the chessboard and its pieces
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                piece = board[row][col]
                if piece != "--":
                    self.screen.blit(self.IMAGES[piece], p.Rect(col * self.SQ_SIZE, row * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def drawText(self, text):
         # Create a font object with the specified settings
        font = p.font.SysFont('Helvetica', 32, True, True)
    #   text: The text to be displayed.
    #   antialias: Determines if anti-aliasing should be applied to the text (True for smoother edges, False for sharper edges).
    #   color: The color of the text.
        textObject = font.render(text, 0, p.Color('black'))
        # Create a rectangle representing the location and size of the text on the screen
    # The text will be centered horizontally and vertically on the screen
        textLocation = p.Rect(0, 0, self.WIDTH, self.HEIGHT).move(self.WIDTH/2 - textObject.get_width()/2, self.HEIGHT/2 - textObject.get_height()/2)
        self.screen.blit(textObject, textLocation)

    def drawGameState(self, gameState, selectedSquare, board):
        validMoves = gameState.getValidMoves()
        self.drawBoard()
        if selectedSquare:
            self.highlightSquare(self.screen, gameState, validMoves, selectedSquare, board)
        if selectedSquare != ():
            self.drawPieces(board)

    def updateDisplay(self):
        p.display.flip()
        self.clock.tick(self.MAX_FPS)

    def getUserInput(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                return "quit"
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                # Calculate the column index of the clicked square
                col = location[0] // self.SQ_SIZE
                 # Calculate the row index of the clicked square a double / is used as python default divides to a decimal but if you 
                 # // the divide will always be an int.
                row = location[1] // self.SQ_SIZE
                return row, col
            # The user pressed the "Z" key on the keyboard
            elif event.type == p.KEYDOWN:
                if event.key == p.K_z:
                    return "undo"
            elif event.type == p.KEYDOWN:
                if event.key == p.K_r:
                    return "reset"
        # If no relevant user input events were detected, return None
        return None
    
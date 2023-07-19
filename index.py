# This is our driver file. It will be responcible for handling user input and displaying the current GameState object.

import pygame as p

import chessEngine

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

#to load images I will initialize a global dictionary of images. 
#this will be called exactly once in the main

def loadImages():
    pieces =["wP", "bP", "wR","bR", "wB", "bB", "wN", "bN", "wQ", "bQ", "wK", "bK"]
    # Usin this for loop and the dictionary I can access an image by typing IMAGE[dictionary]
    for piece in pieces:
        IMAGES[piece] =p.transform.scale(p.image.load("assets/" +piece+ ".png"), (SQ_SIZE, SQ_SIZE))

#THe main driver will handle user input and handle the graphics.

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gamesState = chessEngine.Gamestate()
    loadImages() # only do this once 
    sqSelected = ()
    playerClicks = []
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        # This will control the mouse event handling.
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #() location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                #After asking myself what would happen if the user clicked the square twice I had to add a way of catching the  miss/wrong click and deal with it.
                if sqSelected == (row,col):
                    sqSelected = () # deselect
                    playerClicks = [] #clear player clicks
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected) # this was designed to append both the first and second click
                if len(playerClicks) == 2: #this will be called after the second click is made causing the move of the piece.
                    move = chessEngine.Move(playerClicks[0], playerClicks[1], gamesState.board)
                    print(move.getChessNotation())
                    gamesState.makeMove(move)
                    sqSelected = ()
                    playerClicks = []

        drawGameState(screen, gamesState)
        clock.tick(MAX_FPS)
        p.display.flip()

# This function is responcible for all the graphics of the current Game State
def drawGameState(screen, gameState):
    # This function will draw the squares on the board.
    drawBoard(screen) 
    #TODO add move suggestion and potencially piece highlighting.(Nice to have)
    # This function will draw the pieces on the draw squares
    drawPieces(screen, gameState.board) 

def drawBoard(screen):
    colours = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            colour = colours[((row+col)%2)]
            p.draw.rect(screen, colour, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
     for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--": # This checks it is not an empty square
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))
main()
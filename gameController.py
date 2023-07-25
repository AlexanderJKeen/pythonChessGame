# chessController.py
class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def runGame(self):
        self.view.initialize()

        running = True
        selectedSquare = None

        while running:
            self.view.drawGameState(self.model, selectedSquare, self.model.board)

            if self.model.checkMate:
                if self.model.whiteToMove:
                    self.view.drawText("Checkmate! Black wins")
                else:
                    self.view.drawText("Checkmate! White wins")
            elif self.model.staleMate:
                    self.view.drawText("Stalemate!")
            
            self.view.updateDisplay()

            userInput = self.view.getUserInput()

            if userInput == "quit":
                running = False
            elif userInput == "undo":
                self.model.undoMove()
            elif userInput == "reset":
                # Create a new instance of GameModel to reset the board
                self.model = GameModel() 
                selectedSquare = None
            elif isinstance(userInput, tuple):
                row, col = userInput
                if self.model.isValidSquare(row, col):
                    if selectedSquare:
                        move = self.model.movePiece(selectedSquare, (row, col))
                        if move:
                            self.model.makeMove(move)
                        selectedSquare = None
                    else:
                        selectedSquare = (row, col)
                else:
                    selectedSquare = None


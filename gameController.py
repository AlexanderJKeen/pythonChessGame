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

                # Check if the game is in a checkmate or stalemate state and display the appropriate message
            if self.model.checkMate:
                if self.model.whiteToMove:
                    self.view.drawText("Checkmate! Black wins")
                else:
                    self.view.drawText("Checkmate! White wins")
            elif self.model.staleMate:
                self.view.drawText("Stalemate!")

                # Update the display to show the current game state and messages
            self.view.updateDisplay()

                # Get user input from the GameView object
            userInput = self.view.getUserInput()

                # Process user input based on the action requested
            if userInput == "quit":
                    # Quit the game loop if the player wants to quit
                running = False
            elif userInput == "undo":
                    # Undo the last move if the player requests to undo
                self.model.undoMove()
            elif isinstance(userInput, tuple):
                    # If the user clicks on a square, handle piece selection and movement logic
                row, col = userInput
                if self.model.isValidSquare(row, col):
                    if selectedSquare:
                        # If a piece is already selected, attempt to move it to the clicked square
                        move = self.model.movePiece(selectedSquare, (row, col))
                        if move:
                            # If the move is valid, make the move on the GameModel
                            self.model.makeMove(move)
                        selectedSquare = None
                    else:
                        # If no piece is selected, set the clicked square as the selected square
                        selectedSquare = (row, col)
                else:
                    # If an invalid square is clicked, deselect the selected square
                    selectedSquare = None


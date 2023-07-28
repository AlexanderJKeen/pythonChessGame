# Importing necessary modules
from gameModel import GameModel
from gameView import GameView
from gameController import GameController
from gameMenu import GameMenu
import pygame as p

#     The main function of the game that initializes the game components
#    and controls the game loop.
def main():

    # Create the GameMenu object and initialize it
    menu = GameMenu()
    menu.initialize()
    # Create the GameModel, GameView, and GameController objects
    model = GameModel()
    view = GameView()
    controller = GameController(model, view)
    
    while True:
        # Run the game menu loop and get the user's choice
        menuOption = menuLoop(menu)
        # If the user chooses "New Game", start the game using the controller
        if menuOption == "New Game":
            controller.runGame()
        # If the user chooses "Quit", exit the game
        elif menuOption == "Quit":
            p.quit()
            break

def menuLoop(menu):

    while True:
        # Draw the game menu on the screen
        menu.drawMenu()
        # Update the display to show the menu
        menu.updateDisplay()
        # Get user input to check if the user wants to start a new game or quit
        userInput = menu.getUserInput()
        # Check the user's input and return the corresponding menu option
        if userInput == "quit":
            return "Quit"
        elif userInput == "New Game":
            return "New Game"

if __name__ == "__main__":
    main()

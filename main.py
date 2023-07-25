# main.py
from gameModel import GameModel
from gameView import GameView
from gameController import GameController
from gameMenu import GameMenu
import pygame as p

def main():
    # Create the model, view, and controller objects
    menu = GameMenu()
    menu.initialize()
    model = GameModel()
    view = GameView()
    controller = GameController(model, view)
    
    while True:
        menuOption = menuLoop(menu)
        if menuOption == "New Game":
            controller.runGame()
        elif menuOption == "Quit":
            p.quit()
            break

def menuLoop(menu):
    while True:
        menu.drawMenu()
        menu.updateDisplay()
        userInput = menu.getUserInput()
        if userInput == "quit":
            return "Quit"
        elif userInput == "New Game":
            return "New Game"

if __name__ == "__main__":
    main()

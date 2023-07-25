import pygame as p

class GameMenu:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 900
        self.screen = None
        self.clock = None
        self.menuFont = None
        self.menuOptions = ["New Game", "Quit"]
        self.selectedOption = 0

    def initialize(self):
        p.init()
        self.screen = p.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = p.time.Clock()
        self.menuFont = p.font.Font(None, 64)

    def drawMenu(self):
        self.screen.fill(p.Color("white"))
        for i, option in enumerate(self.menuOptions):
            color = p.Color("black")
            if i == self.selectedOption:
                color = p.Color("red")
            text = self.menuFont.render(option, True, color)
            textRect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + i * 100))
            self.screen.blit(text, textRect)

    def updateDisplay(self):
        p.display.flip()
        self.clock.tick(15)

    def getUserInput(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                return "quit"
            elif event.type == p.KEYDOWN:
                if event.key == p.K_UP:
                    self.selectedOption = (self.selectedOption - 1) % len(self.menuOptions)
                elif event.key == p.K_DOWN:
                    self.selectedOption = (self.selectedOption + 1) % len(self.menuOptions)
                elif event.key == p.K_RETURN:
                    return self.menuOptions[self.selectedOption]
        return None

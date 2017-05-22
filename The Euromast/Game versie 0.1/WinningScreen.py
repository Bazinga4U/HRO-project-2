"""
@copyright Create by De Vijf Musketiers
@content this class shows the winning screen and animation?!?!
"""
import pygame
import Text
import Button
import Music

class WinningScreen:
    def __init__(self, screenWidth, screennHeigt,gameScreen):
        self.width = screenWidth
        self.height = screennHeigt

        self.name = ""
        self.colorWhite = (244, 244, 244)

        self.backgroundImage = pygame.image.load('img/pepe.png')  # image voor background
        self.gameScreen = gameScreen
        self.ExitGame = True
        self.text = Text.Text(gameScreen)
        self.menuButtonWidth = 230 
        self.menuButtonHeight = 50
        self.x_postionButton = 50
        self.y_postionButton0 = 50
        #class
        self.Button = Button.Button
        wit = (244, 244, 244)
        self.black = (49, 49, 49)
        self.menuButton0 = self.Button(wit,wit,self.black,wit,25,gameScreen,self.menuButtonWidth,self.menuButtonHeight,self.x_postionButton,self.y_postionButton0, '')        
        #Music
        self.music = Music.Music('winner')
        #vars
        self.backgroundImage = pygame.image.load('img/pepe.png')  # image voor background
        self.gameOver = False
        self.text = Text.Text(gameScreen)
    def SetWinningPawn(self, name):
        self.name = name
    def AnimateWinningScreen(self):
        self.music.playMusic(True)
        self.gameScreen.blit(self.backgroundImage, (0, 0))
        self.text.DrawText(self.name, 500, 520, self.colorWhite, 100)
        self.menuButton0.DrawButton()
        self.text.DrawText("Back to menu", 90, 60, self.black, 35)
    def WinningScreenHandler(self):
        for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit() #overbodig?
                xMousePos, yMousePos = pygame.mouse.get_pos()
                if events.type == pygame.MOUSEBUTTONUP:
                    if xMousePos > self.x_postionButton and yMousePos > self.y_postionButton0 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton0 + self.menuButtonHeight):
                        self.gameOver = True
"""
@copyright Create by De Vijf Musketiers
@content a class that shows the setting screen
"""
import pygame
import Button
import Text

class SettingScreen:
    def __init__(self,gameDisplay,screenWidth,screenHeight,gameSettings):
        self.screenWidth = screenWidth 
        self.screenHeight = screenHeight 
        self.gameDisplay = gameDisplay
        self.gameSettings = gameSettings
        self.backgroundImage = pygame.image.load('img/default_background.jpg')
        self.gameSettings = gameSettings
        #vars voor de layer
        self.backGroundLayerWidth = ((screenWidth / 100) * 55)
        self.backGroundLayerHeight = ((screenHeight / 100) * 80)
        self.backGroundLayerPostionX = ((screenWidth / 100) * 3)
        self.backGroundLayerPostionY = ((screenHeight / 100) * 10)
        self.backgroundColorScreen = (28,48,128)
        self.backgroundColorLayer = (27,10,47)
        self.buttonLeftSideX = ((screenWidth / 100 * 5))
        self.buttonLeftSideY = ((screenHeight / 100) * 30)
        self.buttonRightSideX = ((screenWidth / 100 * 37))
        self.buttonRightSideY = ((screenHeight / 100) * 30)
    def ShowSettings(self):
        self.ShowBackground()

        buttonColor = (255, 255, 255)
        optionsTextColor = (127,154,184)
        backButton = (255, 255, 255)
        blackColor = (0, 0, 0)


        text = Text.Text(self.gameDisplay)
        text.DrawText("Settings menu", (self.backGroundLayerPostionX + 170), (self.backGroundLayerPostionY + 20), buttonColor, 55)
        text.DrawText("MUSIC", (self.backGroundLayerPostionX + 260), (self.backGroundLayerPostionY + 155), buttonColor, 35)
        text.DrawText("AI DIFFICULTY", (self.backGroundLayerPostionX + 215), (self.backGroundLayerPostionY + 255), buttonColor, 35)
        text.DrawText("DICE ANIMATION", (self.backGroundLayerPostionX + 200), (self.backGroundLayerPostionY + 355), buttonColor, 35)

        if self.gameSettings['musicOn']:
            pygame.draw.rect(self.gameDisplay, buttonColor, ((self.buttonLeftSideX), self.buttonLeftSideY, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))
            pygame.draw.rect(self.gameDisplay, optionsTextColor, ((self.buttonRightSideX), self.buttonRightSideY, self.backGroundLayerWidth / 5,self.backGroundLayerHeight / 10))
        else:
            pygame.draw.rect(self.gameDisplay, optionsTextColor, ((self.buttonLeftSideX), self.buttonLeftSideY, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))
            pygame.draw.rect(self.gameDisplay, buttonColor, ((self.buttonRightSideX), self.buttonRightSideY, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))


        if self.gameSettings['diceAnimationOn']:
            pygame.draw.rect(self.gameDisplay, buttonColor, ((self.buttonLeftSideX), self.buttonLeftSideY + 200, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))
            pygame.draw.rect(self.gameDisplay, optionsTextColor, ((self.buttonRightSideX), self.buttonRightSideY + 200, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))
        else:
            pygame.draw.rect(self.gameDisplay, optionsTextColor, ((self.buttonLeftSideX), self.buttonLeftSideY + 200, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))
            pygame.draw.rect(self.gameDisplay, buttonColor, ((self.buttonRightSideX), self.buttonRightSideY + 200, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))

        if self.gameSettings['aiDifficulty'] == "normal":
            pygame.draw.rect(self.gameDisplay, buttonColor, ((self.buttonLeftSideX), self.buttonLeftSideY + 100, self.backGroundLayerWidth / 5,self.backGroundLayerHeight / 10))
            pygame.draw.rect(self.gameDisplay, optionsTextColor, ((self.buttonRightSideX), self.buttonRightSideY + 100, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))
        else:
            pygame.draw.rect(self.gameDisplay, optionsTextColor, ((self.buttonLeftSideX), self.buttonLeftSideY + 100, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))
            pygame.draw.rect(self.gameDisplay, buttonColor, ((self.buttonRightSideX), self.buttonRightSideY + 100, self.backGroundLayerWidth / 5,self.backGroundLayerHeight / 10))




        # dit wordt knop om terug te gaan naar het hoofdmenu
        pygame.draw.rect(self.gameDisplay, backButton, ((self.buttonLeftSideX) + 210, self.buttonLeftSideY + 330, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 8))
        text.DrawText("Go back", (self.buttonLeftSideX + 230), (self.buttonLeftSideY + 350), blackColor, 35)

        # dit zijn de opties van de settings
        text.DrawText("On", (self.buttonLeftSideX + 50), (self.buttonLeftSideY + 15), blackColor, 35)
        text.DrawText("Off", (self.buttonLeftSideX + 460), (self.buttonLeftSideY + 15), blackColor, 35)
        text.DrawText("Easy", (self.buttonLeftSideX + 40), (self.buttonLeftSideY + 115), blackColor, 35)
        text.DrawText("Hard", (self.buttonLeftSideX + 450), (self.buttonLeftSideY + 115), blackColor, 35)
        text.DrawText("On", (self.buttonLeftSideX + 50), (self.buttonLeftSideY + 215), blackColor, 35)
        text.DrawText("Off", (self.buttonLeftSideX + 460), (self.buttonLeftSideY + 215), blackColor, 35)

    def ShowBackground(self):
        self.gameDisplay.blit(self.backgroundImage, (0, 0)) #Giving the screen a clear background again.
        #Drawing the scoreboard design 
        pygame.draw.rect(self.gameDisplay, self.backgroundColorLayer, ((self.backGroundLayerPostionX), self.backGroundLayerPostionY,self.backGroundLayerWidth-100,self.backGroundLayerHeight))
        pygame.draw.rect(self.gameDisplay, self.backgroundColorScreen, ((self.backGroundLayerPostionX+2), (self.backGroundLayerPostionY+2),(self.backGroundLayerWidth-104),(self.backGroundLayerHeight-4)))
        pygame.draw.rect(self.gameDisplay, self.backgroundColorLayer, ((self.backGroundLayerPostionX+4), (self.backGroundLayerPostionY+4),(self.backGroundLayerWidth-108),(self.backGroundLayerHeight-8)))
        pygame.draw.rect(self.gameDisplay, self.backgroundColorScreen, ((self.backGroundLayerPostionX+6), (self.backGroundLayerPostionY+6),(self.backGroundLayerWidth-112),(self.backGroundLayerHeight-12)))

    def EventHandler(self):
        for events in pygame.event.get():
            xMousePos, yMousePos = pygame.mouse.get_pos()
            if events.type == pygame.QUIT: #wil die stopen... dan stoppen we
                  pygame.quit()
                  quit() #overbodig?] #5 = quit game = break loop
            if events.type == pygame.MOUSEBUTTONUP:
                if xMousePos > (self.buttonLeftSideX + 210) and yMousePos > (self.buttonLeftSideY + 330 ) and xMousePos < ((self.buttonLeftSideX + 210) + self.backGroundLayerWidth / 5) and yMousePos < (self.buttonLeftSideY + 330 + self.backGroundLayerHeight / 8):
                    return True

                elif xMousePos > (self.buttonLeftSideX) and yMousePos > (self.buttonLeftSideY) and xMousePos < ((self.buttonLeftSideX) + self.backGroundLayerWidth / 5) and yMousePos < (self.buttonLeftSideY + self.backGroundLayerHeight / 10):
                    self.gameSettings['musicOn'] = True
                elif xMousePos > (self.buttonLeftSideX + 410) and yMousePos > (self.buttonLeftSideY) and xMousePos < ((self.buttonLeftSideX + 410) + self.backGroundLayerWidth / 5) and yMousePos < (self.buttonLeftSideY + self.backGroundLayerHeight / 10):
                    self.gameSettings['musicOn'] = False

                elif xMousePos > (self.buttonLeftSideX) and yMousePos > (self.buttonLeftSideY + 200) and xMousePos < ((self.buttonLeftSideX) + self.backGroundLayerWidth / 5) and yMousePos < (self.buttonLeftSideY + 200 + self.backGroundLayerHeight / 10):
                    self.gameSettings['diceAnimationOn'] = True
                elif xMousePos > (self.buttonLeftSideX + 410) and yMousePos > (self.buttonLeftSideY + 200) and xMousePos < ((self.buttonLeftSideX + 410) + self.backGroundLayerWidth / 5) and yMousePos < (self.buttonLeftSideY + 200 + self.backGroundLayerHeight / 10):
                    self.gameSettings['diceAnimationOn'] = False

                elif xMousePos > (self.buttonLeftSideX) and yMousePos > (self.buttonLeftSideY + 100) and xMousePos < ((self.buttonLeftSideX) + self.backGroundLayerWidth / 5) and yMousePos < (self.buttonLeftSideY + 100 + self.backGroundLayerHeight / 10):
                    self.gameSettings['aiDifficulty'] = "normal"
                elif xMousePos > (self.buttonLeftSideX + 410) and yMousePos > (self.buttonLeftSideY + 100) and xMousePos < ((self.buttonLeftSideX + 410) + self.backGroundLayerWidth / 5) and yMousePos < (self.buttonLeftSideY + 100 + self.backGroundLayerHeight / 10):
                    self.gameSettings['aiDifficulty'] = "hard"


        return False



"""
@copyright 2017 Created by De Vijf Musketiers
@content this class shows the game rules
"""
import pygame
import Text

class GameRules:
    def __init__(self,screenWidth,screenHeight,gameDisplay):
        self.backGroundLayerWidth = ((screenWidth / 100) * 55)
        self.backGroundLayerHeight = ((screenHeight / 100) * 80)
        self.backGroundLayerPostionX = ((screenWidth / 100) * 3)
        self.backGroundLayerPostionY = ((screenHeight / 100) * 1)
        self.gameDisplay = gameDisplay
        self.buttonLeftSideX = ((screenWidth / 100 * 3))
        self.buttonLeftSideY = ((screenHeight / 100) * 89)
        self.gameRules = ["page1", "page2"]
        self.gameRulesState = self.gameRules[0]
        self.text = Text.Text(self.gameDisplay)

    def showGameRules(self):
        if self.gameRulesState == self.gameRules[0]:
            rules_image = pygame.image.load('img/gamerules.jpg') 
        else:
            rules_image = pygame.image.load('img/shortcuts.jpg')
        self.gameDisplay.blit(rules_image, (0, 0))
        buttonColor = (25,25,25)
        textColor = (244,244,244)


        pygame.draw.rect(self.gameDisplay, buttonColor, ((self.buttonLeftSideX + 12), self.buttonLeftSideY, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))
        pygame.draw.rect(self.gameDisplay, buttonColor, ((self.buttonLeftSideX + 228), self.buttonLeftSideY, self.backGroundLayerWidth / 5, self.backGroundLayerHeight / 10))

       
        self.text.DrawText("Go back", (self.buttonLeftSideX + 44), (self.buttonLeftSideY + 15), textColor, 30)

        if self.gameRulesState == self.gameRules[0]:
            self.text.DrawText("Shortcuts", (self.buttonLeftSideX + 250), (self.buttonLeftSideY + 15), textColor, 30)
        else:
            self.text.DrawText("Game Rules", (self.buttonLeftSideX + 240), (self.buttonLeftSideY + 15), textColor, 30)

    def ExitGameRulesScreen(self):
        for events in pygame.event.get():
            xMousePos, yMousePos = pygame.mouse.get_pos()
            if events.type == pygame.QUIT: #wil die stopen... dan stoppen we
                  pygame.quit()
                  quit() #overbodig?] #5 = quit game = break loop
            if events.type == pygame.MOUSEBUTTONUP:
                if xMousePos > (self.buttonLeftSideX + 12) and yMousePos > (self.buttonLeftSideY) and xMousePos < ((self.buttonLeftSideX + 12) + self.backGroundLayerWidth / 5) and yMousePos < (self.buttonLeftSideY + self.backGroundLayerHeight / 10):
                    self.gameRulesState == self.gameRules[0]
                    return True
                if xMousePos > (self.buttonLeftSideX + 228) and yMousePos > (self.buttonLeftSideY) and xMousePos < ((self.buttonLeftSideX + 228) + self.backGroundLayerWidth / 5) and yMousePos < (self.buttonLeftSideY + self.backGroundLayerHeight / 10):
                    if self.gameRulesState == self.gameRules[0]:
                        self.gameRulesState = self.gameRules[1]
                    else:
                        self.gameRulesState = self.gameRules[0]
            if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_UP:
                            self.gameRulesState = self.gameRules[0]
                        elif events.key == pygame.K_DOWN:
                            self.gameRulesState = self.gameRules[1]
        return False

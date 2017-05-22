"""
@copyright 2017 Created by De Vijf Musketiers
@content a class that shows the content of the scoreboard.
"""

import pygame
import Text
import Database
import Button

class Scoreboard:
    def __init__(self,gameDisplay,screenWidth,screenHeight):
        #Colors
        self.colorDarkBlue = (27,10,47)
        self.colorWhite = (255,255,255)
        self.colorBlue = (28,48,128)
        #Basic vars       
        self.backgroundColorScreen = (28,48,128)
        self.backgroundColorLayer = (27,10,47)
        self.textColor = (0,0,0)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.gameDisplay =  gameDisplay
        #vars to show the scoreboard
        self.scoreboardWidth = 420
        self.scoreboardHeight = 500
        self.scoreboardPostionX = 60
        self.scoreboardPostionY = 50
        #vars to show the exit button
        self.exitButtonWidth = 200
        self.exitButtonHeigth = 50
        self.exitButtonPostionX = 960 
        self.exitButtonPostionY = 50
        #instances
        self.Text = Text.Text(gameDisplay)
        self.connect = Database.Connect()
        #query
        self.GetPlayers =  self.connect.download_scores()
        
        #image var
        self.fontSize = pygame.font.Font("freesansbold.ttf", 20) #font selection
        self.backgroundImage = pygame.image.load('img/default_background.jpg') #Image for background
        #Exit button
        textSize = 20
        self.exitButton = Button.Button(self.colorDarkBlue, self.colorBlue,self.colorWhite, self.colorWhite,textSize,self.gameDisplay,self.exitButtonWidth,self.exitButtonHeigth,self.exitButtonPostionX,self.exitButtonPostionY, 'Return to menu')
    def ExitScoreboardScreen(self): #Method that gives the exit button an working fucntion
        for events in pygame.event.get():
                xMousePos, yMousePos = pygame.mouse.get_pos() #Tracing the X and Y coordinates of the mouse on the game screen. 
                if events.type == pygame.MOUSEBUTTONUP: #When the mousebutton is pressed, it checks if the mouse is placed on top of the exit button
                    if xMousePos > (self.exitButtonPostionX) and yMousePos > (self.exitButtonPostionY) and xMousePos < (self.exitButtonPostionX + (self.exitButtonWidth)) and yMousePos < ((self.exitButtonPostionY) + (self.exitButtonHeigth)):
                        return True
                if xMousePos > (self.exitButtonPostionX) and yMousePos > (self.exitButtonPostionY) and xMousePos < (self.exitButtonPostionX + self.exitButtonWidth) and yMousePos < (self.exitButtonPostionY + self.exitButtonHeigth):
                     self.exitButton.ChangeColor()
                else:
                     self.exitButton.ChangeColorBack() 
                if events.type == pygame.QUIT: 
                    pygame.quit()
                    quit() #onnodig?
        self.exitButton.drawButtonWithLayer()
        return False
    def ShowScoreBoard(self):
        self.DrawScoreboardLayers()
        self.DrawScores()
    def DrawScores(self): #Draws the text on the screen
        self.Text.DrawText("Scoreboard", 210,10,(255,255,255),45)
        #self.Text.DrawText("Return to menu", 970,65,(255,255,255),25)
        self.DrawEachPlayer(self.GetPlayers)
    def DrawEachPlayer(self,players): #Shows the player name with position in the scoreboard.
        y = 60
        for i in range(0,(len(players))):
            self.Text.DrawText("#" + str(i+1), 70,y,(255,255,255),45)
            self.Text.DrawText(str(players[i][0]), 140,y,(255,255,255),45)
            self.Text.DrawText(str(players[i][1]), 430,y,(255,255,255),45)
            y += 50
    #teken layers
    def DrawScoreboardLayers(self):
        self.gameDisplay.blit(self.backgroundImage, (0, 0)) #Giving the screen a clear background again.
        #Drawing the scoreboard design 
        pygame.draw.rect(self.gameDisplay, self.backgroundColorLayer, ((self.scoreboardPostionX), self.scoreboardPostionY,self.scoreboardWidth-100,self.scoreboardHeight))
        pygame.draw.rect(self.gameDisplay, self.backgroundColorScreen, ((self.scoreboardPostionX+2), (self.scoreboardPostionY+2),(self.scoreboardWidth-104),(self.scoreboardHeight-4)))
        pygame.draw.rect(self.gameDisplay, self.backgroundColorLayer, ((self.scoreboardPostionX+4), (self.scoreboardPostionY+4),(self.scoreboardWidth-108),(self.scoreboardHeight-8)))
        pygame.draw.rect(self.gameDisplay, self.backgroundColorScreen, ((self.scoreboardPostionX+6), (self.scoreboardPostionY+6),(self.scoreboardWidth-112),(self.scoreboardHeight-12)))
        #Drawing the second scoreboard rectangle.
        pygame.draw.rect(self.gameDisplay, self.backgroundColorLayer, ((self.scoreboardPostionX+350), self.scoreboardPostionY,self.scoreboardWidth-280,self.scoreboardHeight))
        pygame.draw.rect(self.gameDisplay, self.backgroundColorScreen, ((self.scoreboardPostionX+352), (self.scoreboardPostionY+2),(self.scoreboardWidth-284),(self.scoreboardHeight-4)))
        pygame.draw.rect(self.gameDisplay, self.backgroundColorLayer, ((self.scoreboardPostionX+354), (self.scoreboardPostionY+4),(self.scoreboardWidth-288),(self.scoreboardHeight-8)))
        pygame.draw.rect(self.gameDisplay, self.backgroundColorScreen, ((self.scoreboardPostionX+356), (self.scoreboardPostionY+6),(self.scoreboardWidth-292),(self.scoreboardHeight-12)))
        #Drawing the exit button rectangle.
        #pygame.draw.rect(self.gameDisplay, self.backgroundColorLayer, ((self.exitButtonPostionX), (self.exitButtonPostionY),(self.exitButtonWidth),(self.exitButtonHeigth)))
        #pygame.draw.rect(self.gameDisplay, self.backgroundColorScreen, ((self.exitButtonPostionX+2), (self.exitButtonPostionY+2),(self.exitButtonWidth-4),(self.exitButtonHeigth-4)))
        #pygame.draw.rect(self.gameDisplay, self.backgroundColorLayer, ((self.exitButtonPostionX+4), (self.exitButtonPostionY+4),(self.exitButtonWidth-8),(self.exitButtonHeigth-8)))
        #pygame.draw.rect(self.gameDisplay, self.backgroundColorScreen, ((self.exitButtonPostionX+6), (self.exitButtonPostionY+6),(self.exitButtonWidth-12),(self.exitButtonHeigth-12)))


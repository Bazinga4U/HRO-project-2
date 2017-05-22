"""
@copyright 2017 Created by De Vijf Musketiers
@content This class is used to make buttons
"""
import pygame

#om buttons aan te maken
class Button:
    def __init__(self, color, color2,textColor,newColor,fontSize,gameDisplay,width, height,postion_x,postion_y,text):
        self.backgroundColor = color
        self.backgroundColor2 = color2
        self.textColor = textColor
        self.width = width
        self.height = height
        self.fontSize = pygame.font.Font("freesansbold.ttf", fontSize)
        self.gameDisplay = gameDisplay
        self.postion_x = postion_x
        self.postion_y = postion_y
        self.text = text
        self.newColor = newColor
        self.oldColor = color
        self.newTextColor = color
        self.oldLayerColor = color2
        self.newLayercolor = color
        self.hover = False



    def ChangeColor(self):
        self.textColor = self.newTextColor
        self.backgroundColor = self.newColor
        self.backgroundColor2 = self.newLayercolor
        self.hover = True
        
    def ChangeColorBack(self):
        self.textColor = self.newColor
        self.backgroundColor = self.oldColor
        self.backgroundColor2 = self.oldLayerColor
        self.hover = self.hover = False

    def drawButtonWithLayer(self):
        if self.hover:
            # pygame.draw.rect(gameDisplay, (0,0,255), ((postion_x - 2),(postion_y - 2),(self.width + 5),(self.height + 5))) (e.v.t. randje?)
            pygame.draw.rect(self.gameDisplay, self.backgroundColor2, (self.postion_x,self.postion_y,self.width,self.height)) #eerste layer
            pygame.draw.rect(self.gameDisplay, self.backgroundColor, ((self.postion_x+2),(self.postion_y+2),(self.width-4),(self.height-4))) #tweede layer
            pygame.draw.rect(self.gameDisplay, self.backgroundColor2, ((self.postion_x+4),(self.postion_y+4),(self.width-8),(self.height-8))) #derde layer
            pygame.draw.rect(self.gameDisplay, self.backgroundColor, ((self.postion_x+6),(self.postion_y+6),(self.width-12),(self.height-12))) #button zelf tekenen
            self.gameDisplay.blit(self.fontSize.render(self.text, True, self.textColor), ((self.postion_x + (self.width / 5)),(self.postion_y + (self.height / 4)))) #tekst van de button teken
        else:
            pygame.draw.rect(self.gameDisplay, self.backgroundColor, (self.postion_x,self.postion_y,self.width,self.height)) #eerste layer
            pygame.draw.rect(self.gameDisplay, self.backgroundColor2, ((self.postion_x+2),(self.postion_y+2),(self.width-4),(self.height-4))) #tweede layer
            pygame.draw.rect(self.gameDisplay, self.backgroundColor, ((self.postion_x+4),(self.postion_y+4),(self.width-8),(self.height-8))) #derde layer
            pygame.draw.rect(self.gameDisplay, self.backgroundColor2, ((self.postion_x+6),(self.postion_y+6),(self.width-12),(self.height-12))) #button zelf tekenen
            self.gameDisplay.blit(self.fontSize.render(self.text, True, self.textColor), ((self.postion_x + (self.width / 5)),(self.postion_y + (self.height / 4)))) #tekst van de button teken       
    def DrawButton(self):
            # pygame.draw.rect(gameDisplay, (0,0,255), ((postion_x - 2),(postion_y - 2),(self.width + 5),(self.height + 5))) (e.v.t. randje?)
            pygame.draw.rect(self.gameDisplay, self.backgroundColor, (self.postion_x, self.postion_y,self.width,self.height)) #button zelf tekenen
            self.gameDisplay.blit(self.fontSize.render(self.text, True, self.textColor), ((self.postion_x + (self.width / 5)),(self.postion_y + (self.height / 4)))) #tekst van de button teken
    #speciale button voor de timer
    def DrawTimerButton(self,seconds):
        # pygame.draw.rect(gameDisplay, (0,0,255), ((postion_x - 2),(postion_y - 2),(self.width + 5),(self.height + 5))) (e.v.t. randje?)
        pygame.draw.rect(self.gameDisplay, self.backgroundColor, (self.postion_x, self.postion_y,self.width,self.height)) #button zelf tekenen
        self.gameDisplay.blit(self.fontSize.render(str(seconds), True, self.textColor), ((self.postion_x + (self.width / 5)),(self.postion_y + (self.height / 4)))) #tekst van de button teken
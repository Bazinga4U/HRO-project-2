"""
@copyright Create by De Vijf Musketiers
@content this class makes a the dice roll and handels the animation
"""
import pygame
import random
import time
import Timer
import Music

class Dice:
    def __init__(self, gameDisplay, screenWidth, screenHeight,diceAnimation):
        self.backgroundColor = (27,10,47)
        self.textColor = (255,255,255)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.gameDisplay =  gameDisplay
        self.gameScreenStates = ['Boardgame', 'Dice']
        self.gameScreenCurrentState = self.gameScreenStates[0]
        #vars
        self.diceAnimation = diceAnimation
        #vars to show the dice button
        self.diceButtonWidth = 150
        self.diceButtonHeigth = 60
        self.diceButtonPostionX = ((screenWidth / 100) * 2)
        self.diceButtonPostionY = ((screenHeight / 100) * 5)
        self.fontSize = pygame.font.Font("freesansbold.ttf", 20) #font selection
        self.diceImages = ["img/dices/dice1.jpg","img/dices/dice2.jpg","img/dices/dice3.jpg","img/dices/dice4.jpg","img/dices/dice5.jpg","img/dices/dice6.jpg"]
        self.diceImages2 = ["img/dices/dice1.jpg","img/dices/dice2.jpg","img/dices/dice3.jpg","img/dices/dice4.jpg","img/dices/dice5.jpg","img/dices/dice6.jpg"]
        #instans
        self.Timer = Timer.Timer(gameDisplay)
        #Music
        self.music = Music.Music('dice')
        self.musicOn = True
    #event handler voor player
    def DrawDiceButton(self):
        pygame.draw.rect(self.gameDisplay, self.backgroundColor, ((self.diceButtonPostionX), self.diceButtonPostionY, self.diceButtonWidth, self.diceButtonHeigth))
        self.gameDisplay.blit(self.fontSize.render('Roll Dice', True, self.textColor), ((self.diceButtonPostionX + (self.diceButtonWidth / 5)),(self.diceButtonPostionY + (self.diceButtonHeigth / 4))))

        for events in pygame.event.get():
            xMousePos, yMousePos = pygame.mouse.get_pos()
            if events.type == pygame.MOUSEBUTTONUP:
                if xMousePos > self.diceButtonPostionX and yMousePos > self.diceButtonPostionY and xMousePos < (self.diceButtonPostionX + self.diceButtonWidth) and yMousePos < (self.diceButtonPostionY + self.diceButtonHeigth):
                    return True
            if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RETURN:
                        return True
        return False
    #dice result voor speler
    def ShowDiceResult(self):
        result = self.ThrowDice()
        if self.diceAnimation == True:
            self.AnimateDiceRoll(result)
        self.ShowDiceImage(result)
        return self.CorrectResult(result)
    #dice result voor AI
    def ShowAIDiceResult(self,result):
        if self.diceAnimation == True:
            self.AnimateDiceRoll(result)
        self.ShowDiceImage(result)
        return self.CorrectResult(result)
    #dice result voor 'AI' en 'human' player
    def ThrowDice(self):
        result = random.randint(1,6)
        return result
    def CorrectResult(self,result):
        if result == 1 or result == 2:
            return 1
        elif result == 3 or result == 4:
            return 2
        else:
            return 3
    def ShowDiceImage(self,result):
        self.Timer.StartTimer(2)
        while not self.Timer.RunOutOfTime:
             image = pygame.image.load(self.diceImages[result-1])
             self.gameDisplay.blit(image,(self.diceButtonPostionX,self.diceButtonPostionY))
             pygame.display.update()
             self.Timer.CheckTimer()
             for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit() 
        self.Timer.RunOutOfTime = False
    def AnimateDiceRoll(self,result):
        self.SoundDiceRoll()
        self.Timer.StartTimer(5)
        while not self.Timer.RunOutOfTime:
            randomArray = self.diceImages2  
            random.shuffle(randomArray)
            for i in range(0,3):
                image = pygame.image.load(randomArray[i])
                self.gameDisplay.blit(image,(self.diceButtonPostionX,self.diceButtonPostionY))
                time.sleep(0.2)
                pygame.display.update()
            self.Timer.CheckTimer()
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit() 
        self.Timer.RunOutOfTime = False
        self.StopDiceRoll()
    def SoundDiceRoll(self):
        self.music.playMusic(True)
    def StopDiceRoll(self):
        self.music.stopMusic()
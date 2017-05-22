"""
@copyright 2017 Created by De Vijf Musketiers
@content this class makes a player instance
"""
import pygame
import random
import Timer

class AIplayer:
    def __init__(self,difficultyLevel):
        self.aiDifficulty = difficultyLevel
        self.directionArray = ['up','left','right']
    def MoveDirection(self):
        if self.aiDifficulty == "normal":
            x = random.randint(0,1) #1/2 omhoog, te moeilijk?
            if x != 0:
                 x = random.randint(1,2) 
        else:
            x = 0 #iets te moeilijk?
        return self.directionArray[x] 
    def TrowDice(self):
        if self.aiDifficulty == "normal":
            x = random.randint(1,6) #default dice
        else:
            x = random.randint(4,6) #gooit 1/3 keer 2 en 2/3 6
        return x
    def ChooseCategory(self,categoriesLeft):
        if categoriesLeft[0] == True:
            return 0
        elif categoriesLeft[1] == True:
            return 1
        elif categoriesLeft[2] == True:
            return 2
        elif categoriesLeft[3] == True:
            return 3
    def AnswerQuestion(self,answer):
        array = ["A","B","C","D"]
        Timer.time.sleep(1)
        if self.aiDifficulty == "normal":
            chooseAnswer = array[random.randint(0,3)]
        else:
            if answer == "A" or answer == "B":
                chooseAnswer = array[random.randint(0,1)]
            else: 
                chooseAnswer = array[random.randint(2,3)]
        if chooseAnswer == answer:
            return True
        else:
            return False
"""
@copyright Create by De Vijf Musketiers
@content this class gets the questions and check if they are answered correctly
"""
import pygame
import Button
import os

class Question:
    def __init__(self,gameDisplay,screenWidth,screenHeight):
        #kleuren
        self.colorRed = (255,00,00) 
        self.colorBlack = (00,00,00)

        #vars om te kaart te tonen
        self.currentRedCard = 0 
        self.currentGreenCard = 0
        self.currentBlueCard = 0 
        self.currentYellowCard = 0
        self.currentQuestion = None
        self.questionAwnser = None
        self.questionAsked = False
        self.playerAnswer = None
        self.question = ''
        self.awnser = ''
        self.correctAnswer = ""
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.gameDisplay = gameDisplay
        #button instants
        self.Button = Button.Button
        #postions bepalen van de buttons om de image
        self.questionButtonWidth = 750 #button code same as in controller
        self.questionButtonHeight = 25

        self.buttonSize = (self.questionButtonWidth,self.questionButtonHeight)

        self.x_postionButton1 = ((self.screenWidth / 100) * 25)
        self.y_postionButton1 = ((self.screenHeight / 100) * 25) + 28

        self.x_postionButton2 = ((self.screenWidth / 100) * 25)
        self.y_postionButton2 = ((self.screenHeight / 100) * 25)  + 52

        self.x_postionButton3 = ((self.screenWidth / 100) * 25)
        self.y_postionButton3 = ((self.screenHeight / 100) * 25) + 79

        self. x_postionButton4 = ((self.screenWidth / 100) * 25)
        self.y_postionButton4 = ((self.screenHeight / 100) * 25) + 100
    def SetQuestion(self,category):
        
        if category == 'blue': #if player is on a blue space
            path = 'img/cards/blue'
            amountOfBlueCards = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
            blueCards = [f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))] 
            if amountOfBlueCards == self.currentBlueCard: # if all blue cards are used
                self.currentBlueCard = 0
                self.currentQuestion =  'img/cards/blue/' + blueCards[self.currentBlueCard]
                self.questionAwnser = blueCards[self.currentBlueCard] # zorgt dat de kaarten niet opraken tijdens het testen
                self.currentBlueCard += 1
                #return False # als de kaarten op zijn
            else:
                self.currentQuestion =  'img/cards/blue/' + blueCards[self.currentBlueCard]
                self.questionAwnser = blueCards[self.currentBlueCard]
                self.currentBlueCard += 1 #the next time on starts on a blue space it will have the next question
        elif category == 'red': #if player is on a red space
            path = 'img/cards/red'
            amountOfRedCards = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
            redCards =[f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))]
            if amountOfRedCards == self.currentRedCard: #if player is on a red space
                self.currentRedCard = 0
                self.currentQuestion = 'img/cards/red/' + redCards[self.currentRedCard] # zorgt dat de kaarten niet opraken tijdens het testen
                self.questionAwnser = redCards[self.currentRedCard]
                self.currentRedCard += 1
                #return False # als de kaarten op zijn
            else:
                self.currentQuestion = 'img/cards/red/' + redCards[self.currentRedCard]
                self.questionAwnser = redCards[self.currentRedCard]
                self.currentRedCard += 1 #the next time on starts on a red space it will have the next question
        elif category == 'yellow': #if player is on a yellow space
            path = 'img/cards/yellow'
            amountOfYellowCards = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
            yellowCards =[f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))]
            if amountOfYellowCards == self.currentYellowCard: #if player is on a yellow space
                self.currentYellowCard = 0
                self.currentQuestion = 'img/cards/yellow/' + yellowCards[self.currentYellowCard] # zorgt dat de kaarten niet opraken tijdens het testen
                self.questionAwnser = yellowCards[self.currentYellowCard]
                self.currentYellowCard += 1
                #return False # als de kaarten op zijn
            else:
                self.currentQuestion = 'img/cards/yellow/' + yellowCards[self.currentYellowCard]
                self.questionAwnser = yellowCards[self.currentYellowCard]
                self.currentYellowCard += 1 #the next time on starts on a yellow space it will have the next question
        elif category == 'green': #if player is on a green space
            path = 'img/cards/Green'
            amountOfGreenCards = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
            greenCards =[f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))]
            if amountOfGreenCards == self.currentGreenCard: #if player is on a green space
                self.currentGreenCard = 0
                self.currentQuestion = 'img/cards/Green/' + greenCards[self.currentGreenCard] # zorgt dat de kaarten niet opraken tijdens het testen
                self.questionAwnser = greenCards[self.currentGreenCard]
                self.currentGreenCard += 1
                #return False # als de kaarten op zijn
            else:
                self.currentQuestion = 'img/cards/Green/' + greenCards[self.currentGreenCard]
                self.questionAwnser = greenCards[self.currentGreenCard]
                self.currentGreenCard += 1 #the next time on starts on a green space it will have the next question
        self.questionAsked = True

    def showQuestion(self):
        question_image = pygame.image.load(self.currentQuestion)
        question_image_x_position = ((self.screenWidth / 100) * 25)
        question_image_y_position = (self.screenHeight / 100) * 25
        
        self.gameDisplay.blit(question_image, (question_image_x_position, question_image_y_position)) 

    def getAnswerForAI(self):
        if self.questionAwnser.endswith('A.jpg') == True:
            self.correctAnswer = "A"
            return "A"
        elif self.questionAwnser.endswith('B.jpg') == True:
            self.correctAnswer = "B"
            return "B"
        elif self.questionAwnser.endswith('C.jpg') == True:
            self.correctAnswer = "C"
            return "C"
        elif self.questionAwnser.endswith('D.jpg') == True:
            self.correctAnswer = "D"
            return "D"
    def IfAnswerIsCorrect(self):
        if self.questionAwnser.endswith('A.jpg') == True:
            self.correctAnswer = "A"
        elif self.questionAwnser.endswith('B.jpg') == True:
            self.correctAnswer = "B"
        elif self.questionAwnser.endswith('C.jpg') == True:
            self.correctAnswer = "C"
        elif self.questionAwnser.endswith('D.jpg') == True:
            self.correctAnswer = "D"

        if self.correctAnswer == self.playerAnswer:
            return True
        else:
            return False
    def QuestionButton(self):   
        for events in pygame.event.get():
            if events.type == pygame.MOUSEBUTTONUP:
                xMousePos, yMousePos = pygame.mouse.get_pos()
                if xMousePos > self.x_postionButton1 and yMousePos > self.y_postionButton1 and xMousePos < (self.x_postionButton1 + self.questionButtonWidth) and yMousePos < (self.y_postionButton1 + self.questionButtonHeight) : #makes button work
                    self.playerAnswer = "A"
                    print('A')
                    return True
                elif xMousePos > self.x_postionButton2 and yMousePos > self.y_postionButton2 and xMousePos < (self.x_postionButton2 + self.questionButtonWidth) and yMousePos < (self.y_postionButton2 + self.questionButtonHeight): 
                    self.playerAnswer = "B"
                    print('B')
                    return True
                elif xMousePos > self.x_postionButton3 and yMousePos > self.y_postionButton3 and xMousePos < (self.x_postionButton3 + self.questionButtonWidth) and yMousePos < (self.y_postionButton3 + self.questionButtonHeight): 
                    self.playerAnswer = "C"
                    print('C')
                    return True
                elif xMousePos > self.x_postionButton4 and yMousePos > self.y_postionButton4 and xMousePos < (self.x_postionButton4 + self.questionButtonWidth) and yMousePos < (self.y_postionButton4 + self.questionButtonHeight): 
                    self.playerAnswer = "D"
                    print('D')
                    return True
                #shortcuts
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_a:
                    self.playerAnswer = "A"
                    return True
                elif events.key == pygame.K_b:
                    self.playerAnswer = "B"
                    return True
                elif events.key == pygame.K_c:
                    self.playerAnswer = "C"
                    return True
                elif events.key == pygame.K_d:
                    self.playerAnswer = "D"
                    return True
            if events.type == pygame.QUIT:
               pygame.quit()
               quit() #overbodig?
        return False
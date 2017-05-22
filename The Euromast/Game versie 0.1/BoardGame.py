"""
@copyright Create by De Vijf Musketiers
@content this class shows all objects on the Gameboard
"""
import pygame
import Text


class GameBoard:
    def __init__(self, width, height,gameScreen):
        self.width = width
        self.height = height


        #redouan isn't cool
        self.arrowleftImage = pygame.image.load('img/arrowleft.png')
        self.arrowrightImage = pygame.image.load('img/arrowright.png')
        self.arrowupImage = pygame.image.load('img/arrowup.png')
        self.dirction = pygame.image.load('img/chosedirection.png')
        self.backgroundImage = pygame.image.load('img/board.jpg')  # image voor background
        self.pauseMenuImage = pygame.image.load('img/pause.jpg')  # image voor background
        self.gameSavedImage = pygame.image.load('img/game_saved.jpg')
        self.gameScreen = gameScreen   
        self.GetGridPostion() #haal de start postions op
        #instantes
        self.text = Text.Text(gameScreen)
        #DrawStartPostions
        self.startPostionX = ((self.width / 100) * 20)
        self.startPostionY = ((self.height / 100) * 20)
        self.startPostionWidthScreen = ((self.width / 100) * 60)
        self.startPostionHeightScreen = ((self.height / 100) * 60)
        self.colorWhite = (244, 244, 244)
        self.lichtBlack = (49, 49, 49)
        #pick category vars
        self.PickCategoryPostionX =  ((self.width / 100) * 20)
        self.PickCategoryPostionY = ((self.height / 100) * 20)
        self.PickCategoryWidthScreen =  ((self.width / 100) * 60)
        self.PickCategoryHeightScreen = ((self.height / 100) * 60)
        self.categoryButtonWidthScreen = ((self.PickCategoryWidthScreen / 100) * 80)
        self.categoryButtonHeightScreen =  ((self.PickCategoryHeightScreen / 100) * 15)
        self.categoryButtonXpost = self.PickCategoryPostionX + ((self.PickCategoryPostionX / 100) * 30)
        self.categoryButton1 = (37,117,170) 
        self.categoryButton2 = (217,30,25) 
        self.categoryButton3 = (244,172,52)
        self.categoryButton4 = (31,130,76)
        self.categoryButtonDark = (94,95,95)
        self.categoryButtonYpost1 = self.PickCategoryPostionY + ((self.PickCategoryHeightScreen / 100) * 10) 
        self.categoryButtonYpost2 = self.PickCategoryPostionY + ((self.PickCategoryHeightScreen / 100) * 30) 
        self.categoryButtonYpost3 = self.PickCategoryPostionY + ((self.PickCategoryHeightScreen / 100) * 50) 
        self.categoryButtonYpost4 = self.PickCategoryPostionY + ((self.PickCategoryHeightScreen / 100) * 70) 
        
    #teken board game
    def DrawBoard(self):
        self.gameScreen.blit(self.backgroundImage, (0, 0))  #start van board
    #teken de pawns op het board
    def DrawPawn(self,pawn,x_pos,y_pos):
        self.gameScreen.blit(pawn,(x_pos,y_pos)) 
    #hier komt het scherm met hoeveel spelers wilt u spelen + naam invullen + AI kiezen
    def ShowChooseScreen(self):
        return 1
    #in deze method kan er een direction board getekend waar de speler op kan klikken
    def DrawDirection(self):
        self.gameScreen.blit(self.arrowleftImage, (20, 100))
        self.gameScreen.blit(self.arrowrightImage, (127, 100))
        self.gameScreen.blit(self.arrowupImage, (73, 50))
        self.gameScreen.blit(self.dirction, (27, 20))
    #teken het pauze menu
    def DrawPauseMenu(self):
        self.gameScreen.blit(self.pauseMenuImage, (0, 0))  #start van board
    #teken het draw menu
    def DrawStartPostions(self):
        pygame.draw.rect(self.gameScreen, self.lichtBlack, (self.startPostionX, self.startPostionY, self.startPostionWidthScreen , self.startPostionHeightScreen))       
        self.text.DrawText("We will now determine the start positions.", (self.startPostionX + 50), (self.startPostionY + 50), self.colorWhite, 35)
        self.text.DrawText("There will be a dice roll for each player.", (self.startPostionX + 50), (self.startPostionY + 75), self.colorWhite, 35)
        self.text.DrawText("This dice roll will be automatic!", (self.startPostionX + 50), (self.startPostionY + 100), self.colorWhite, 35)
        self.text.DrawText("If it’s a draw, a winner will still be pick.", (self.startPostionX + 50), (self.startPostionY + 150), self.colorWhite, 35)
        self.text.DrawText("The player with the highest dice number may choose first.", (self.startPostionX + 50), (self.startPostionY + 175), self.colorWhite, 35)
        self.text.DrawText("The player that threw the number first will win.", (self.startPostionX + 50), (self.startPostionY + 200), self.colorWhite, 35)

    #teken het menu category
    def DrawPickCategory(self,categoriesLeft,playername):
         pygame.draw.rect(self.gameScreen, self.lichtBlack, (self.PickCategoryPostionX, self.PickCategoryPostionY, self.PickCategoryWidthScreen , self.PickCategoryHeightScreen))
         self.text.DrawText("Player " + playername + " may choose a category!", (self.categoryButtonXpost + 100), (self.PickCategoryPostionY + 20), self.colorWhite, 35)
         #button een
         if categoriesLeft[0] == True:
            pygame.draw.rect(self.gameScreen, self.categoryButton1, (self.categoryButtonXpost + 10, self.categoryButtonYpost1 + 20, self.categoryButtonWidthScreen , self.categoryButtonHeightScreen))
            self.text.DrawText("Sports", (self.categoryButtonXpost + 265), (self.categoryButtonYpost1 + 40), self.colorWhite, 35)
         else:
            pygame.draw.rect(self.gameScreen, self.categoryButtonDark, (self.categoryButtonXpost + 10, self.categoryButtonYpost1 + 20, self.categoryButtonWidthScreen , self.categoryButtonHeightScreen))
         #button twee
         if categoriesLeft[1] == True:
            pygame.draw.rect(self.gameScreen, self.categoryButton2, (self.categoryButtonXpost + 10, self.categoryButtonYpost2 + 20, self.categoryButtonWidthScreen , self.categoryButtonHeightScreen))
            self.text.DrawText("Entertaiment", (self.categoryButtonXpost + 235), (self.categoryButtonYpost2 + 40), self.colorWhite, 35)
         else:
            pygame.draw.rect(self.gameScreen, self.categoryButtonDark, (self.categoryButtonXpost + 10, self.categoryButtonYpost2 + 20, self.categoryButtonWidthScreen , self.categoryButtonHeightScreen))
         #button drie
         if categoriesLeft[2] == True:
            pygame.draw.rect(self.gameScreen, self.categoryButton3, (self.categoryButtonXpost + 10, self.categoryButtonYpost3 + 20, self.categoryButtonWidthScreen , self.categoryButtonHeightScreen))
            self.text.DrawText("Histoy", (self.categoryButtonXpost + 265), (self.categoryButtonYpost3 + 40), self.colorWhite, 35)
         else:
            pygame.draw.rect(self.gameScreen, self.categoryButtonDark, (self.categoryButtonXpost + 10, self.categoryButtonYpost3 + 20, self.categoryButtonWidthScreen , self.categoryButtonHeightScreen))
         #button vier
         if categoriesLeft[3] == True:
            pygame.draw.rect(self.gameScreen, self.categoryButton4, (self.categoryButtonXpost + 10, self.categoryButtonYpost4 + 20, self.categoryButtonWidthScreen , self.categoryButtonHeightScreen))
            self.text.DrawText("Geography", (self.categoryButtonXpost + 235), (self.categoryButtonYpost4 + 40), self.colorWhite, 35)
         else:
            pygame.draw.rect(self.gameScreen, self.categoryButtonDark, (self.categoryButtonXpost + 10, self.categoryButtonYpost4 + 20, self.categoryButtonWidthScreen , self.categoryButtonHeightScreen))
    #haal de naam postitie
    def GetNewPostion(self,currentPost,direction,diceRoll):
        rowNumber = int(currentPost[3])
        if currentPost[3]  == "1":
            if currentPost[4] == "0" or currentPost[4] == "1" or currentPost[4] == "2" or currentPost[4] == "3" or currentPost[4] == "4" or currentPost[4] == "5" or currentPost[4] == "6":
                rowNumber = int(str("1" + currentPost[4]))
        try:
            xPost =  int(currentPost[-3]) #voor het geval dat het 'blue','red','yellow is'
        except ValueError:
            xPost = 0
        if direction == "up":
            rowNumber += int(diceRoll)
            if rowNumber > 15:
                return 'row16'
            elif rowNumber > 10:
                x = currentPost[-5:]
                if x == "['1']" and (rowNumber - diceRoll) <= 10 or x == "['2']" and (rowNumber - diceRoll) <= 10:
                    return 'row' + str(rowNumber) + "['1']"
                elif x == "['3']" and (rowNumber - diceRoll) <= 10 or x == "['4']"  and (rowNumber - diceRoll) <= 10:
                     return 'row' + str(rowNumber) + "['2']"
                elif x == "['5']" and (rowNumber - diceRoll) <= 10 or x == "['6']" and (rowNumber - diceRoll) <= 10:
                     return 'row' + str(rowNumber) + "['3']"
                elif x == "['7']" and (rowNumber - diceRoll) <= 10 or x == "['8']" and (rowNumber - diceRoll) <= 10:
                     return 'row' + str(rowNumber) + "['4']"
                else:
                    return 'row' + str(rowNumber) + "['" +  str(currentPost[-3:])
            else:
                if currentPost == "row0[blue]":
                    return 'row' + str(rowNumber) + "['1']"
                elif currentPost == "row0[red]":
                     return 'row' + str(rowNumber) + "['3']"
                elif currentPost == "row0[yellow]":
                     return 'row' + str(rowNumber) + "['5']"
                elif currentPost == "row0[green]":
                     return 'row' + str(rowNumber) + "['7']"
                else:
                    return 'row' + str(rowNumber) + "['" +  str(currentPost[-3:])
        elif direction == "right":
            xPost += int(diceRoll)
            if rowNumber > 15:
                return 'row16'
            elif rowNumber > 10:
                if xPost > 4:
                    if xPost == 5:
                        xPost = 1
                    elif xPost == 6:
                        xPost = 2
                    elif xPost == 7:
                        xPost = 3
                    else:
                        xPost = 4 #kan niet voorkomen
                return 'row' + str(rowNumber) + "['" + str(xPost) + "']"
            elif rowNumber > 0:
                if xPost > 8:
                    if xPost == 9:
                        xPost = 1
                    elif xPost == 10:
                        xPost = 2
                    elif xPost == 11:
                        xPost = 3
                    else:
                        xPost = 4 #kan niet voorkomen
                return 'row' + str(rowNumber) + "['" + str(xPost) + "']"
            else:
                return self.GetNewPostion(currentPost,"up",diceRoll) #als je nog niet op vakje 1 staat, dan ga je naar na boven
        elif direction == "left":
            xPost -= int(diceRoll)
            if rowNumber > 15:
                return 'row16'
            elif rowNumber > 10:
                if xPost < 1:
                    if xPost == -3:
                        xPost = 2
                    elif xPost == -2:
                        xPost = 3
                    elif xPost == -1 or xPost == 0:
                        xPost = 4
                    else:
                        xPost = 2 #kan niet voorkomen
                return 'row' + str(rowNumber) + "['" + str(xPost) + "']"
            elif rowNumber > 0:
                if xPost < 1:
                    if xPost == -1 or xPost == 0:
                        xPost = 8
                    elif xPost == -2:
                        xPost = 7
                    elif xPost == -3:
                        xPost = 3
                    else:
                        xPost = 4 #kan niet voorkomen
                return 'row' + str(rowNumber) + "['" + str(xPost) + "']"
            else:
                return self.GetNewPostion(currentPost,"up",diceRoll) #als je nog niet op vakje 1 staat, dan ga je naar na boven
        else:
                return self.GetNewPostion(currentPost,"up",diceRoll)
    #teken het game saved scherm
    def DrawGameSavedMenu(self):
        self.gameScreen.blit(self.gameSavedImage, (0, 0))  #start van board
    #teken board screen
    def DrawDataOnGameBoard(self,player,turn):
        self.text.DrawText("Player turn:", (self.width - 190), ((self.height / 100) * 1), (0,255,0),40)
        self.text.DrawText(player.name, (self.width - 190), ((self.height / 100) * 6), (0,255,0),40)
        self.text.DrawText("Players Pawn", (self.width - 190), ((self.height / 100) * 10), (0,255,0),40)
        self.gameScreen.blit(player.pawn,((self.width - 190),((self.height / 100) * 15)))
    #beweeg de pawn
    def MovePawn(self,NewPost):
        selfNewPost = "self." + NewPost #eval(ab)
        return eval(selfNewPost)
    #zet hier de start positie speler in
    def StartPostionPlayers(self,category):
        x,y = self.row0[category]
        name = "row0[" + str(category) + "]" #str niet echt nodig
        return x,y,name
    def GetCategory(self,postionName):
        rowNumber = int(postionName[3]) 
        if postionName[3]  == "1":
            if postionName[4] == "0" or postionName[4] == "1" or postionName[4] == "2" or postionName[4] == "3" or postionName[4] == "4" or postionName[4] == "5" or postionName[4] == "6":
                rowNumber = int(str("1" + postionName[4]))
        if rowNumber == 0:
           category = postionName[5]
           if category == "b":
               return 'blue'
           elif category == "r":
               return 'red'
           elif category == "y":
               return 'yellow'
           elif category == "g":
               return 'green'
        elif rowNumber > 0 and rowNumber < 11:
           x = postionName[-5:]
           if x == "['1']":
               return 'blue'
           elif x == "['2']":
               return 'blue'
           elif x == "['3']":
               return 'red'
           elif  x == "['4']":
               return 'red'
           elif  x == "['5']":
               return 'yellow'
           elif x == "['6']":
               return 'yellow'
           elif x == "['7']":
               return 'green'
           elif x == "['8']":
               return 'green'
        elif rowNumber > 10:
           x = postionName[-5:]
           if x == "['3']":
               return 'blue'
           elif x == "['4']":
               return 'red'
           elif x == "['2']":
               return 'yellow'
           elif x == "['1']":
               return 'green'
        return None #verbeteren?
    def GetGridPostion(self):
        #Let op! Om de benamening klein te houden is er gekozen voor bekropte benaming
        #deze vars zijn voor de start postions
        y0 = 666
        #Deze vars van de eerste 10 rows
        y1 = 652
        y2 = 620
        y3 = 588
        y4 = 554
        y5 = 518
        y6 = 486
        y7 = 449
        y8 = 414
        y9 = 376
        y10 = 337

        x1 = 189
        x2 = 274
        x3 = 456
        x4 = 535
        x5 = 714
        x6 = 793
        x7 = 977
        x8 = 1051
         #Deze vars/constant van de eerste 15 rows
        y11 = 270
        y12 = 210
        y13 = 156
        y14 = 90
        y15 = 30
        topX1 = 235
        topX2 = 491
        topX3 = 755
        topX4 = 1018
        #de row voor de start postions
        self.row0 = {"blue": (x1,y0),"red": (x3,y0),"yellow": (x5,y0),"green": (x7,y0)}
        #de eerste 10 rows
        self.row1 = { "1": (x1,y1), "2" :(x2,y1),"3": (x3,y1), "4" :(x4,y1),"5": (x5,y1), "6" :(x6,y1),"7": (x7,y1), "8" :(x8,y1) }
        self.row2 = { "1": (x1,y2), "2" :(x2,y2),"3": (x3,y2), "4" :(x4,y2),"5": (x5,y2), "6" :(x6,y2),"7": (x7,y2), "8" :(x8,y2) }
        self.row3 = { "1": (x1,y3), "2" :(x2,y3),"3": (x3,y3), "4" :(x4,y3),"5": (x5,y3), "6" :(x6,y3),"7": (x7,y3), "8" :(x8,y3) }
        self.row4 = { "1": (x1,y4), "2" :(x2,y4),"3": (x3,y4), "4" :(x4,y4),"5": (x5,y4), "6" :(x6,y4),"7": (x7,y4), "8" :(x8,y4) }
        self.row5 = { "1": (x1,y5), "2" :(x2,y5),"3": (x3,y5), "4" :(x4,y5),"5": (x5,y5), "6" :(x6,y5),"7": (x7,y5), "8" :(x8,y5) }
        self.row6 = { "1": (x1,y6), "2" :(x2,y6),"3": (x3,y6), "4" :(x4,y6),"5": (x5,y6), "6" :(x6,y6),"7": (x7,y6), "8" :(x8,y6) }
        self.row7 = { "1": (x1,y7), "2" :(x2,y7),"3": (x3,y7), "4" :(x4,y7),"5": (x5,y7), "6" :(x6,y7),"7": (x7,y7), "8" :(x8,y7) }
        self.row8 = { "1": (x1,y8), "2" :(x2,y8),"3": (x3,y8), "4" :(x4,y8),"5": (x5,y8), "6" :(x6,y8),"7": (x7,y8), "8" :(x8,y8) }
        self.row9 = { "1": (x1,y9), "2" :(x2,y9),"3": (x3,y9), "4" :(x4,y9),"5": (x5,y9), "6" :(x6,y9),"7": (x7,y9), "8" :(x8,y9) }
        self.row10 = { "1": (x1,y10), "2" :(x2,y10),"3": (x3,y10), "4" :(x4,y10),"5": (x5,y10), "6" :(x6,y10),"7": (x7,y10), "8" :(x8,y10) }
        #de laatse 5 rows
        self.row11 = { "1": (topX1,y11), "2" :(topX2,y11),"3": (topX3,y11), "4" :(topX4,y11) }
        self.row12 = { "1": (topX1,y12), "2" :(topX2,y12),"3": (topX3,y12), "4" :(topX4,y12) }
        self.row13 = { "1": (topX1,y13), "2" :(topX2,y13),"3": (topX3,y13), "4" :(topX4,y13) }
        self.row14 = { "1": (topX1,y14), "2" :(topX2,y14),"3": (topX3,y14), "4" :(topX4,y14) }
        self.row15 = { "1": (topX1,y15), "2" :(topX2,y15),"3": (topX3,y15), "4" :(topX4,y15) }
        #de winnaar post
        self.row16 = (0,0)
"""
@copyright Create by De Vijf Musketiers
@content this class connects all the classes, methods needed to run the game. Also execute the same code
"""
import pygame
import Timer
import Question
import BoardGame
import Player
import Dice
import Text
import GameRules
import Button
import WinningScreen
import Input
import AIplayer
import Database

class Game:
    def __init__(self,gameDisplay,screenWidth,screenHeight,gameSettings):
        #instances
        self.boardGame = BoardGame.GameBoard(screenWidth, screenHeight,gameDisplay)
        self.timer = Timer.Timer(self.boardGame)
        self.winningScreen = WinningScreen.WinningScreen(screenWidth, screenHeight,gameDisplay)
        self.dice = Dice.Dice(gameDisplay,screenWidth,screenHeight,gameSettings['diceAnimationOn'])
        self.gameRules = GameRules.GameRules(screenWidth,screenHeight,gameDisplay) #connect met gameRules
        self.Question = Question.Question(gameDisplay,screenWidth,screenHeight)
        self.Input1 = Input.Input() #kan dit in de array? controlleer later.
        self.Input2 = Input.Input()
        self.Input3 = Input.Input()
        self.Input4 = Input.Input()
        self.database = Database.Connect()
        #vars (Python ken geen constants)
        self.amountOfPlayers = 0 #tel hoeveel spelers er spelen
        self.gameOver = False #als de game over is breekt de loop
        self.inGame = False #ondermeer handig voor een pauze optie
        self.categories = ('blue','red','green','yellow')
        self.player = {} #array waar de spelers in kunnen
        self.gameDisplay = gameDisplay
        self.screenWidth = screenWidth 
        self.screenHeight = screenHeight
        #state handler
        self.gameStates = ['chooseDirection','rollDice','question','resultQuestion','nextTurn','winning screen']
        self.currentGamestate = None
        #array voor player turn
        self.playerTurns = { 'playerID': None,'direction': None, 'diceRoll': None,'answerCorrect ': True }
        #buttons
        self.buttonX = (screenWidth - 190)
        self.buttonY = ((screenHeight / 100) * 25)
        self.buttonY1 = ((screenHeight / 100) * 30)
        self.buttonY2 = ((screenHeight / 100) * 35)
        self.buttonWidth = 190
        self.buttonHeight = 30
        textSize = 20
        #gamesettings waaronder
        self.aiDifficulty = gameSettings['aiDifficulty']
        self.diceAnimation = gameSettings['diceAnimationOn']
        self.musicOn = gameSettings['musicOn']
        #var voor "ai"/computerspeler
        self.computerPlayer = AIplayer.AIplayer(self.aiDifficulty)
        #voor naam invoeren
        self.namePlayers = [0,self.Input1,self.Input2,self.Input3,self.Input4] #0 is een verbeteringspunt
        #self.menuButton4 = self.Button(self.colorDarkBlue, self.colorBlue,self.colorWhite, self.colorWhite,textSize,self.gameDisplay,self.menuButtonWidth,self.menuButtonHeight,self.x_postionButton,self.y_postionButton4, 'Quit game')
        self.button = Button.Button((27,10,47),(27,10,47),(255,255,255), (255,255,255),textSize, gameDisplay,self.buttonWidth,self.buttonHeight,self.buttonX, self.buttonY, 'Game rules')
        self.button1 = Button.Button((27,10,47),(27,10,47),(255,255,255), (255,255,255),textSize, gameDisplay,self.buttonWidth,self.buttonHeight,self.buttonX, self.buttonY1, 'Save Game')
        self.button2 = Button.Button((27,10,47),(27,10,47),(255,255,255), (255,255,255),textSize, gameDisplay,self.buttonWidth,self.buttonHeight,self.buttonX, self.buttonY2, 'Exit game')
        #timer button
        self.timerButtonWidth = 100
        self.timerButtonnHeight = 100
        self.timerButtonX = 0
        self.timerButtonY = 0
        self.timerButton = Button.Button((27,10,47),(27,10,47),(255,255,255), (255,255,255),textSize, gameDisplay,self.timerButtonWidth,self.timerButtonnHeight,self.timerButtonX, self.timerButtonY, '')
        #overig vars (wel in gebruik!)
        self.rangePlayersID = 0
        self.winnerDeclared = False
        self.winnerId = None
        self.isStartPostionsSet = False
        #om te starts postions te bepalen
        self.currentPostionPlayers = {} #array met player ID's die een postitie hebt
        self.categorieOptionsLeft = [True,True,True,True]
        self.startPostionsState = ['makePlayers','rollDice','choseWinner','choseCategory','playAgain']
        self.currentStartPostionsState = self.startPostionsState[0]
        self.winnnerDiceRoll = 0
        #insert
        self.insertedWinner = False

    #dit is de while loop die zorgt dat de game blijft in de loop
    def RunGame(self):
        while not self.gameOver: #stop de game als die over is of gestopt is
            self.DrawBoard() #teken het bord en zet postions van het board vast + teken de rest van het bord
            if not self.inGame and self.amountOfPlayers > 1 and self.player: #als de spelers gekozen zijn dan zet het spel klaar om gespeeld te worden (mits nodig)
                self.BeforeTheGame()
            if self.inGame and self.amountOfPlayers  > 1: #wanneer er minder dan 2 spelers zijn kan het spel niet worden gestart
                if not self.isStartPostionsSet:
                    self.StartPostionsSet() #geeft te kans om speler te dobbelen
                else:
                    self.PlayGame() # als de voorwaarde boven kloppen kan het spel worden gespeeld
            else:
                if self.amountOfPlayers > 1:
                    self.DeclarePlayerNames()
                else:
                    self.ChooseAmountPlayers()  # Je moet minimaal 1 pygame.event.get() loop hebben en maximiaal 1!

            pygame.display.update() #update het scherm

    #play the game
    def PlayGame(self):
        if self.currentGamestate == self.gameStates[0]:  #de speler kan een direction kiezen
            self.ChooseDirection()
        elif self.currentGamestate == self.gameStates[1]: #gooi de dobbelsteen
            self.DiceRoll()
        elif self.currentGamestate == self.gameStates[2]: #krijg een vraag en kies een antwoord of de tijd raakt op
            self.AnswerQuestion()
        elif self.currentGamestate == self.gameStates[3]: #resultaat van het de question (true or false?) bepaalt of de pawn van speler beweegt de pawn )
            if self.playerTurns['answerCorrect']  == True:
                self.SetPawnPosition()
            else:
                self.currentGamestate = self.gameStates[4]
        elif self.currentGamestate == self.gameStates[4]: #geeft de beurt aan de volgende speler en reset waardes
            self.GiveTurnToNextPlayer()
        elif self.currentGamestate == self.gameStates[5]: #e.v.t. wordt er een win scherm getoond, als het zover is
            if self.player[self.winnerId].isComputerPlayer == False:
                self.UpdateDatabaseWinnings(self.player[self.winnerId].name)
            self.ShowWinningScreen()
        else:
            pass #404... terug na menu? 
    #hier gaan spelers dobbelen tot dat er een winnaar is!
    def StartPostionsSet(self):
        if self.currentStartPostionsState == self.startPostionsState[0]:
            self.boardGame.DrawStartPostions()
            for i in range(1,(len(self.player) + 1)):
               currentPostionPlayers = {'result' : 0,'hasStartPostion' : False,'id' : i,'Category': 404 }
               self.currentPostionPlayers[i] = currentPostionPlayers
            self.currentStartPostionsState = self.startPostionsState[1]
        elif self.currentStartPostionsState == self.startPostionsState[1]:  #gooi de dobbelsteen automatisch
                self.boardGame.DrawStartPostions()
                for i in range(1,(len(self.player) + 1)):
                   if not self.currentPostionPlayers[i]['hasStartPostion']:
                    self.currentPostionPlayers[i]['result']  = self.dice.ShowDiceResult()
                self.currentStartPostionsState = self.startPostionsState[2]
        elif self.currentStartPostionsState == self.startPostionsState[2]: #kies de winnaar
            self.winnnerDiceRoll = 0
            highestNumberTrow = 0   
            for i in range(1,len(self.currentPostionPlayers)+1):
               if not self.currentPostionPlayers[i]['hasStartPostion']:
                   if highestNumberTrow < self.currentPostionPlayers[i]['result']:
                        self.winnnerDiceRoll = self.currentPostionPlayers[i]['id']
               self.currentStartPostionsState = self.startPostionsState[3]
        elif self.currentStartPostionsState == self.startPostionsState[3]: #laat de winnaar een category kiezen
            clicked = False
            self.boardGame.DrawPickCategory(self.categorieOptionsLeft, self.player[self.winnnerDiceRoll].name)
            if self.player[self.winnnerDiceRoll].isComputerPlayer == True:
                x = self.computerPlayer.ChooseCategory(self.categorieOptionsLeft)
                category = self.categories[x]
                self.categorieOptionsLeft[x] = False
                clicked = True
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        pygame.quit()
                        quit() #overbodig?
            else:
                for events in pygame.event.get():
                    xMousePos, yMousePos = pygame.mouse.get_pos()
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_1 and self.categorieOptionsLeft[0] != False:
                            category = self.categories[0]
                            self.categorieOptionsLeft[0] = False
                            clicked = True
                        elif events.key == pygame.K_2 and self.categorieOptionsLeft[1] != False:
                            category = self.categories[1]
                            self.categorieOptionsLeft[1] = False
                            clicked = True
                        elif events.key == pygame.K_3 and self.categorieOptionsLeft[2] != False:
                            category = self.categories[2]
                            self.categorieOptionsLeft[2] = False
                            clicked = True
                        elif events.key == pygame.K_4 and self.categorieOptionsLeft[3] != False:
                            category = self.categories[3]
                            self.categorieOptionsLeft[3] = False
                            clicked = True
                    if events.type == pygame.MOUSEBUTTONUP:
                        if xMousePos > self.boardGame.categoryButtonXpost and yMousePos > self.boardGame.categoryButtonYpost1 and xMousePos < (self.boardGame.categoryButtonXpost + self.boardGame.categoryButtonWidthScreen) and yMousePos < (self.boardGame.categoryButtonYpost1 + self.boardGame.categoryButtonHeightScreen):
                            category = self.categories[0]
                            #self.categories = ('blue','red','green','yellow')
                            self.categorieOptionsLeft[0] = False
                            clicked = True
                        elif xMousePos > self.boardGame.categoryButtonXpost and yMousePos > self.boardGame.categoryButtonYpost2 and xMousePos < (self.boardGame.categoryButtonXpost + self.boardGame.categoryButtonWidthScreen) and yMousePos < (self.boardGame.categoryButtonYpost2 + self.boardGame.categoryButtonHeightScreen):
                            category = self.categories[1]
                            self.categorieOptionsLeft[1] = False
                            clicked = True
                        elif xMousePos > self.boardGame.categoryButtonXpost and yMousePos > self.boardGame.categoryButtonYpost3 and xMousePos < (self.boardGame.categoryButtonXpost + self.boardGame.categoryButtonWidthScreen) and yMousePos < (self.boardGame.categoryButtonYpost3 + self.boardGame.categoryButtonHeightScreen):
                            category = self.categories[3] #yellow
                            self.categorieOptionsLeft[2] = False
                            clicked = True
                        elif xMousePos > self.boardGame.categoryButtonXpost and yMousePos > self.boardGame.categoryButtonYpost4 and xMousePos < (self.boardGame.categoryButtonXpost + self.boardGame.categoryButtonWidthScreen) and yMousePos < (self.boardGame.categoryButtonYpost4 + self.boardGame.categoryButtonHeightScreen):
                            category = self.categories[2] #green
                            self.categorieOptionsLeft[3] = False
                            clicked = True
                    if events.type == pygame.QUIT:
                        pygame.quit()
                        quit() #overbodig?
            if clicked == True:
                x,y,postion = self.boardGame.StartPostionPlayers(category)
                self.currentStartPostionsState = self.startPostionsState[4]
                self.player[self.winnnerDiceRoll].category = category
                self.player[self.winnnerDiceRoll].postionName = postion
                self.player[self.winnnerDiceRoll].x_post = x
                self.player[self.winnnerDiceRoll].y_post = y
                self.currentPostionPlayers[self.winnnerDiceRoll]['hasStartPostion'] = True
        elif self.currentStartPostionsState == self.startPostionsState[4]: #kies de winnaar
            stillPlayersLeft = False
            for i in range(1,len(self.currentPostionPlayers) + 1):
               if not self.currentPostionPlayers[i]['hasStartPostion']: 
                   stillPlayersLeft = True
            if stillPlayersLeft == True:
                self.currentStartPostionsState = self.startPostionsState[1]
            else:
                self.isStartPostionsSet = True
        #self.isStartPostionsSet = True #alleen test later weg halen
    #insert/update value in database
    def UpdateDatabaseWinnings(self,name):
        if self.insertedWinner == False:
            self.database.update_playerscore_table(name)
            self.insertedWinner = True
    #Toon winning scherm
    def ShowWinningScreen(self):
        self.winningScreen.SetWinningPawn(self.player[self.winnerId].name)
        self.winningScreen.AnimateWinningScreen()
        self.winningScreen.WinningScreenHandler()
        self.gameOver = self.winningScreen.gameOver
    #player kan direction kiezen
    def ChooseDirection(self):
        self.boardGame.DrawDirection() #teken een board direction
        if self.player[self.playerTurns['playerID']].isComputerPlayer:
             self.playerTurns['chooseDirection'] = self.computerPlayer.MoveDirection()
             self.currentGamestate = self.gameStates[1]
             self.DefaultForloop()
        else:
            for events in pygame.event.get():
                    xMousePos, yMousePos = pygame.mouse.get_pos()
                    if events.type == pygame.MOUSEBUTTONUP:
                        if xMousePos > 20 and yMousePos > 100 and xMousePos < (20 + 55) and yMousePos < (100 + 54):
                            self.playerTurns['chooseDirection'] = 'left'
                            self.currentGamestate = self.gameStates[1]
                        elif xMousePos > 127 and yMousePos > 100 and xMousePos < (127 + 61) and yMousePos < (100 + 61):
                            self.playerTurns['chooseDirection'] = 'right'
                            self.currentGamestate = self.gameStates[1]
                        elif xMousePos > 73 and yMousePos > 50 and xMousePos < (73 + 56) and yMousePos < (50 + 54):
                            self.playerTurns['chooseDirection'] = 'up'
                            self.currentGamestate = self.gameStates[1]
                    if events.type == pygame.MOUSEBUTTONUP:
                         xMousePos, yMousePos = pygame.mouse.get_pos()
                    if events.type == pygame.KEYDOWN:
                        if events.key == pygame.K_LEFT:
                            self.playerTurns['chooseDirection'] = 'left'
                            self.currentGamestate = self.gameStates[1]
                        elif events.key == pygame.K_RIGHT:
                            self.playerTurns['chooseDirection'] = 'right'
                            self.currentGamestate = self.gameStates[1]
                        elif events.key == pygame.K_UP:
                            self.playerTurns['chooseDirection'] = 'up'
                            self.currentGamestate = self.gameStates[1]
                        elif events.key == pygame.K_DOWN:
                            self.playerTurns['chooseDirection'] = 'down'
                            self.currentGamestate = self.gameStates[1]
                    self.DefaultGameEvents(events)
    #player kan de dobbelsteen gooien
    def DiceRoll(self):
        clicked = self.dice.DrawDiceButton()
        if self.player[self.playerTurns['playerID']].isComputerPlayer:
            diceRoll = self.dice.ShowAIDiceResult(self.computerPlayer.TrowDice())
            self.playerTurns['diceRoll'] = diceRoll
            self.currentGamestate = self.gameStates[2] #uit zetten? 
        if clicked == True:
            diceRoll = self.dice.ShowDiceResult()
            self.playerTurns['diceRoll'] = diceRoll
            self.currentGamestate = self.gameStates[2] #uit zetten? 
    #vraag beantwoorden
    def AnswerQuestion(self): 
        postionName = self.player[self.playerTurns['playerID']].postionName 
        category = self.boardGame.GetCategory(postionName)
        if not self.Question.questionAsked:
            self.Question.SetQuestion(category)
        if not self.timer.timerStarted:
            self.timer.StartTimer(50)
        elif not self.timer.RunOutOfTime:
            self.Question.showQuestion()
            #voor de AI
            if self.player[self.playerTurns['playerID']].isComputerPlayer:
                answerd = self.computerPlayer.AnswerQuestion(self.Question.getAnswerForAI())
                if answerd == True:   
                    self.playerTurns['answerCorrect'] = True
                    self.currentGamestate = self.gameStates[3]
                else:
                    self.playerTurns['answerCorrect'] = False
                    self.currentGamestate = self.gameStates[4]
            if self.Question.QuestionButton() == True:
                answerd = self.Question.IfAnswerIsCorrect()
                if answerd == True:       
                    self.playerTurns['answerCorrect'] = True
                    self.currentGamestate = self.gameStates[3]
                else:
                    self.playerTurns['answerCorrect'] = False
                    self.currentGamestate = self.gameStates[4]
            self.timer.CheckTimer()
            #teken de countdown button
            self.timerButton.DrawTimerButton(self.timer.seconds)
        else:
            self.playerTurns['answerCorrect'] = False
            self.currentGamestate = self.gameStates[4]
    #zet de spelers op de start postie
    def BeforeTheGame(self):
        #for i in range(1,(self.rangePlayersID + 1)): #de i begint met 0, daarom + 1
         #   self.player[i].x_post, self.player[i].y_post,self.player[i].postion = self.boardGame.StartPostionPlayers(self.player[i].category) #haal de start postie
        self.inGame = True #we kunnen het spel gaan spelen!
        #hier komt een 
        self.playerTurns = { 'playerID': 1,'direction': None, 'diceRoll': None,'answerCorrect ': None }
        self.currentGamestate = self.gameStates[0]
    def SetPawnPosition(self):
        for events in pygame.event.get():
                 self.DefaultGameEvents(events)
        #get postion
        newPostionName = self.boardGame.GetNewPostion(self.player[self.playerTurns['playerID']].postionName,self.playerTurns['chooseDirection'],self.playerTurns['diceRoll'])
        if newPostionName == "row16":
            self.winnerId = self.playerTurns['playerID'] #sla de id op
            self.UpdateDatabaseWinnings(self.player[self.playerTurns['playerID']].name) #geeft de naam mee 
            self.winnerDeclared = True
            self.currentGamestate = self.gameStates[5]
        else:
            #move pawn
            x, y = self.boardGame.MovePawn(newPostionName)
            PawnMoved = self.MovePawn(x,y,self.playerTurns['playerID'])
            if PawnMoved == True:
                 self.player[self.playerTurns['playerID']].postionName = newPostionName
                 for i in range(1,(len(self.player)+1)): #de i begint met 0, daarom + 1
                    if self.player[self.playerTurns['playerID']].id !=  self.player[i].id and self.player[self.playerTurns['playerID']].postionName ==  self.player[i].postionName:
                        newPostionName = self.boardGame.GetNewPostion((self.player[i].postionName),'right',self.dice.ShowDiceResult())
                        self.player[i].postionName = newPostionName
                        x, y = self.boardGame.MovePawn(newPostionName)
                        while not self.MovePawn(x,y,i):
                            self.DefaultForloop()
                            pygame.display.update()
                 self.currentGamestate = self.gameStates[4] #verander de gamestate na de volgende stap (give turn to other player)
    #beweegt te de pawn
    def MovePawn(self,x,y,id):
         if x !=  self.player[id].x_post:
                if x > (self.player[id].x_post + 6):
                    if self.player[id].x_post < 15 and self.playerTurns['chooseDirection'] == "left":
                        self.player[id].x_post = (self.screenWidth - 15)
                    elif (x-450) > self.player[id].x_post and self.playerTurns['chooseDirection'] == "left":
                        self.player[id].x_post -= 10
                    else:
                        self.player[id].x_post += 5
                elif x > self.player[id].x_post:
                    self.player[id].x_post += 1
                elif x < (self.player[id].x_post - 6): 
                    if self.player[id].x_post > ((self.screenWidth / 100) * 97) and self.playerTurns['chooseDirection'] == "right":
                        self.player[id].x_post = 15
                    elif (x+450) < self.player[id].x_post and self.playerTurns['chooseDirection'] == "right":
                        self.player[id].x_post += 10
                    else:
                        self.player[id].x_post -= 5
                else:
                    self.player[id].x_post -= 1
         elif y !=  self.player[id].y_post: 
                if y < (self.player[id].y_post - 6):
                    self.player[id].y_post -= 4
                elif y < self.player[id].y_post:
                    self.player[id].y_post -= 1
                elif y > (self.player[id].y_post + 6):
                    self.player[id].y_post += 4
                else:
                    self.player[id].y_post += 1
         else:
            return True
         return False
    #geeft de beurt aan de volgende speler
    def GiveTurnToNextPlayer(self):
        for events in pygame.event.get(): #zodat die niet vast loopt, en dat je op exit kan klikken
                self.DefaultGameEvents(events)
        playerTurn =  self.playerTurns['playerID'] + 1 #de volgende speler laten spelen
        if playerTurn > self.amountOfPlayers: #als de speler niet bestaat dan is speler 1 aan de beurt
            playerTurn = 1
        self.playerTurns = { 'playerID': playerTurn,'direction': None, 'diceRoll': None,'answerCorrect ': None }
        self.timer.timerStarted = False
        self.Question.questionAsked = False

        self.currentGamestate = self.gameStates[0]
    #teken de board op het scherm
    def DrawBoard(self): 
       self.boardGame.DrawBoard() #constant weergave van board
       #zet hier een i waarde
       if self.isStartPostionsSet == True:
           for i in range(1,(len(self.player) + 1)): #de i begint met 0, daarom + 1
            self.boardGame.DrawPawn(self.player[i].pawn,self.player[i].x_post, self.player[i].y_post )
       if self.inGame:
            if self.isStartPostionsSet == True:
                self.boardGame.DrawDataOnGameBoard(self.player[self.playerTurns['playerID']],self.playerTurns)
                self.button.DrawButton()
                self.button1.DrawButton()
                self.button2.DrawButton()
    #Make players is niet verwarren met Makeplayer!
    def MakePlayers(self):
        for i in range(1, (self.amountOfPlayers+1)): #hij stopt anders bij 3
            if self.namePlayers[i].IsEmpty():
                AI = True
            else:
                AI = False
            self.MakePlayer(self.namePlayers[i].value,AI)
    #deze method is om een player instance
    def MakePlayer(self,name,computerPlayer):
         self.rangePlayersID += 1 #totale spelers is net met 1 gestegen
         playerid = self.rangePlayersID #speler id is het nummer dat de spelers is (1,2,3 of 4)
         self.player[playerid] = Player.Player(playerid,name,computerPlayer)
    #save game
    def SaveGame(self):
        # verwijder oude saves
        self.database.deleteSaveGame()
        # waardes in database voegen
        sg_id = 1
        sg_name = 'save game'
        self.database.insertSaveGame(sg_id, sg_name)
        self.database.insertSaveGameTurn(sg_id, self.playerTurns['playerID'])
        for i in range(1, (len(self.player) + 1)):  # de i begint met 0, daarom + 1
            self.database.insertSaveGamePlayers(self.player[i].id, sg_id, self.player[i].x_post, self.player[i].y_post,
                                                self.player[i].postionName, self.player[i].name,
                                                self.player[i].isComputerPlayer)
        self.ShowSavedGameScreen()

    def LoadGame(self, selectLoadGame, selectLoadGamePlayers):
        self.playerTurns = {'playerID': selectLoadGame[0][0], 'direction': None, 'diceRoll': None,
                            'answerCorrect ': None}
        # def MakePlayer(self,name,computerPlayer):
        for i in range(0, len(selectLoadGamePlayers)):
            self.MakePlayer(selectLoadGamePlayers[i][5], selectLoadGamePlayers[i][6])
            x = i + 1
            self.player[x].x_post = selectLoadGamePlayers[i][2]
            self.player[x].y_post = selectLoadGamePlayers[i][3]
            self.player[x].postionName = selectLoadGamePlayers[i][4].replace("*", "'")

        self.isStartPostionsSet = True
        self.amountOfPlayers = len(selectLoadGamePlayers)
        self.inGame = True
        self.currentGamestate = self.gameStates[0]
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()  # overbodig?
    def ShowSavedGameScreen(self):
        savedScreen = True
        self.boardGame.DrawGameSavedMenu()
        pygame.display.update() #update het scherm
        while (savedScreen):
            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONUP or events.type == pygame.KEYDOWN:
                    savedScreen = False
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit() #overbodig?
        
    #deze handler is voor het begin scherm
    def ChooseAmountPlayers(self):
        # achtergrond van de knoppen locatie vastellen
        x_position = ((self.screenWidth / 100) * 25)
        y_position = ((self.screenHeight / 100) * 20)
        widthScreen = ((self.screenWidth / 100) * 50)
        heightScreen = ((self.screenHeight / 100) * 60)

        buttonX_Pos = (x_position * 1.5)
        buttonY_Pos = (y_position + 100)
        color = (49, 49, 49)
        buttonColor = (244, 244, 244)
        buttonTextColor = (49, 49, 49)

        # print achtergrond van menu
        pygame.draw.rect(self.gameDisplay, color, (x_position, y_position, widthScreen, heightScreen))

        # vastellen locatie van knoppen
        pygame.draw.rect(self.gameDisplay, buttonColor, (buttonX_Pos, buttonY_Pos, widthScreen / 2, heightScreen / 6))
        pygame.draw.rect(self.gameDisplay, buttonColor, (buttonX_Pos, y_position + 200, widthScreen / 2, heightScreen / 6))
        pygame.draw.rect(self.gameDisplay, buttonColor, (buttonX_Pos, y_position + 300, widthScreen / 2, heightScreen / 6))

        # titel van menu
        text = Text.Text(self.gameDisplay)
        text.DrawText("Choose amount of players!", (buttonX_Pos - 40), (buttonY_Pos - 50), buttonColor, 45)
        # keuze van aantal spelers
        text.DrawText("2 Players!", (buttonX_Pos + 85), (buttonY_Pos + 20), buttonTextColor, 45)
        text.DrawText("3 Players!", (buttonX_Pos + 85), (buttonY_Pos + 120), buttonTextColor, 45)
        text.DrawText("4 Players!", (buttonX_Pos + 85), (buttonY_Pos + 220), buttonTextColor, 45)

        for events in pygame.event.get():
            if events.type == pygame.MOUSEBUTTONUP:
                xMousePos, yMousePos = pygame.mouse.get_pos()
                if xMousePos > (buttonX_Pos) and yMousePos > (buttonY_Pos) and xMousePos < ((buttonX_Pos) + widthScreen / 2) and yMousePos < (buttonY_Pos + heightScreen / 6):
                    self.amountOfPlayers = 2
                elif xMousePos > (buttonX_Pos) and yMousePos > (y_position + 200) and xMousePos < ((buttonX_Pos) + widthScreen / 2) and yMousePos < (y_position + 200 + heightScreen / 6):
                    self.amountOfPlayers = 3
                elif xMousePos > (buttonX_Pos) and yMousePos > (y_position + 300) and xMousePos < ((buttonX_Pos) + widthScreen / 2) and yMousePos < (y_position + 300 + heightScreen / 6):
                    self.amountOfPlayers = 4
            self.DefaultGameEvents(events)


    def DeclarePlayerNames(self):
        # achtergrond van de knoppen locatie vastellen
        x_position = ((self.screenWidth / 100) * 25)
        y_position = ((self.screenHeight / 100) * 20)
        widthScreen = ((self.screenWidth / 100) * 50)
        heightScreen = ((self.screenHeight / 100) * 75)

        buttonX_Pos = (x_position * 1.5)
        buttonY_Pos = (y_position + 100)
        color = (49, 49, 49)
        buttonColor = (244, 244, 244)
        buttonTextColor = (49, 49, 49)
        backButton = (103, 65, 114)
        startGameButton = (46, 204, 113)
        inputField = (248, 148, 6)

        backButtonLocationY = y_position + 385
        backButtonText4Players = y_position + 405

        # print achtergrond van menu
        pygame.draw.rect(self.gameDisplay, color, (x_position, y_position, widthScreen , heightScreen))
        if self.amountOfPlayers == 4:
            pygame.draw.rect(self.gameDisplay, color, (x_position, y_position, widthScreen, heightScreen))

        text = Text.Text(self.gameDisplay)
        text.DrawText("Enter a name!", (x_position + 215), (y_position + 20), buttonColor, 45)

        buttonY_Pos1 = buttonY_Pos + 90
        buttonY_Pos2 = buttonY_Pos1 + 90
        buttonY_Pos3 = buttonY_Pos2 + 90
        buttonArrayPostY = [0, buttonY_Pos, buttonY_Pos1, buttonY_Pos2, buttonY_Pos3] #0 is een verbeteringspunt

        if self.amountOfPlayers == 4:
            backButtonLocationY += 60
            backButtonText4Players += 60

        pygame.draw.rect(self.gameDisplay, backButton, (x_position + 160, backButtonLocationY, widthScreen / 6, heightScreen / 8))
        pygame.draw.rect(self.gameDisplay, startGameButton, (x_position + 375, backButtonLocationY, widthScreen / 6, heightScreen / 8))
        text.DrawText("*Leave field empty if you want AI", (x_position + 158), (backButtonText4Players - 50), buttonColor, 30)
        text.DrawText("Go back!", (x_position + 170), (backButtonText4Players ), buttonColor, 30)
        text.DrawText("Start!", (x_position + 400), (backButtonText4Players), buttonColor, 30)

        for events in pygame.event.get():
            xMousePos, yMousePos = pygame.mouse.get_pos()
            if events.type == pygame.MOUSEBUTTONUP:
                if xMousePos > (x_position + 160) and yMousePos > (backButtonLocationY) and xMousePos < ((x_position + 160) + widthScreen / 6) and yMousePos < (backButtonLocationY + heightScreen / 8):
                    self.amountOfPlayers = 0
                elif xMousePos > (x_position + 375) and yMousePos > (backButtonLocationY) and xMousePos < ((x_position + 375) + widthScreen / 2) and yMousePos < (backButtonLocationY + 200 + heightScreen / 6):
                   self.MakePlayers()

            for i in range(1, (self.amountOfPlayers + 1)):
                if xMousePos > (buttonX_Pos) and yMousePos > (int(buttonArrayPostY[i]) - 30) and xMousePos < ( (buttonX_Pos) + widthScreen / 6) and yMousePos < (int(buttonArrayPostY[i]) - 30 + heightScreen / 8):
                    self.namePlayers[i].mouseOver = True
                else:
                    self.namePlayers[i].mouseOver = False
                self.namePlayers[i].updateString(events)
            if events.type == pygame.QUIT:
                pygame.quit()
                quit() #overbodig?
        # vastellen locatie van knoppen
        for i in range(1, (self.amountOfPlayers + 1)):
            pygame.draw.rect(self.gameDisplay, buttonColor,(buttonX_Pos, buttonArrayPostY[i] - 30, widthScreen / 2, heightScreen / 8))
            text.DrawText(str(self.namePlayers[i].value), (buttonX_Pos + 10), (buttonArrayPostY[i] - 15), buttonTextColor, 30)
    def DefaultForloop(self):
        for events in pygame.event.get():
            self.DefaultGameEvents(events)
    def DefaultGameEvents(self,events):
        if events.type == pygame.QUIT:
            pygame.quit()
            quit() #overbodig?
        if events.type == pygame.MOUSEBUTTONUP:
            xMousePos, yMousePos = pygame.mouse.get_pos()
            if xMousePos > self.buttonX and yMousePos > self.buttonY and xMousePos < (self.buttonX + self.buttonWidth) and yMousePos < (self.buttonY + self.buttonHeight):
                #game rules)
                while not self.gameRules.ExitGameRulesScreen():
                    self.gameRules.showGameRules()
                    pygame.display.update() #update het scherm
            elif xMousePos > self.buttonX and yMousePos > self.buttonY1 and xMousePos < (self.buttonX + self.buttonWidth) and yMousePos < (self.buttonY1 + self.buttonHeight):
               self.SaveGame()
            elif xMousePos > self.buttonX and yMousePos > self.buttonY2 and xMousePos < (self.buttonX + self.buttonWidth) and yMousePos < (self.buttonY2 + self.buttonHeight):
               #quite game
               self.gameOver = True
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_p:
                self.PauseMenu()
    def PauseMenu(self):
        pauseMenu = True
        self.boardGame.DrawPauseMenu()
        pygame.display.update() #update het scherm
        while (pauseMenu):
            for events in pygame.event.get():
                if events.type == pygame.MOUSEBUTTONUP or events.type == pygame.KEYDOWN:
                    pauseMenu = False
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit() #overbodig?
        
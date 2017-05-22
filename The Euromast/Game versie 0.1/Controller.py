"""
@copyright 2017 Created by De Vijf Musketiers
@content this class is used to start the application/game and give the user(s) the option to run a bit of code
"""
import pygame
import Button
import BoardGame
import GameRules
import Game
import Scoreboard
import Database
import Music
import SetttingScreen


class Controller:
    def __init__(self):
        self.screenWidth = 1280
        self.screenHeight = 700
        size = (self.screenWidth,self.screenHeight)

        # #kleuren
        self.colorDarkBlue = (27,10,47)
        self.colorWhite = (255,255,255)
        self.colorBlue = (28,48,128)

        #vars (Python ken geen constants)
        self.gameScreenStates = ['Menu','Game','loadGame','Settings','Scoreboard','gamerules','Exit']
        self.gameScreenCurrentState = self.gameScreenStates[0] #als deze niet standaard op 0 staat, zet hem op 0
        #scherm
        self.backgroundImage = pygame.image.load('img/default_background.jpg') #image voor background
        self.gameDisplay = pygame.display.set_mode(size)
        #array voor settings
        self.gameSettings = { 'aiDifficulty': "normal",'musicOn': True, 'diceAnimationOn': True }
        #class
        self.Button = Button.Button
        #vars voor de button
        self.menuButtonWidth = 200
        self.menuButtonHeight = 60
        buttonSize = (self.menuButtonWidth,self.menuButtonHeight)
        self.x_postionButton = (self.screenWidth / 9) - (self.menuButtonWidth /9) #de width postitie toevoegen in de array
        self.y_postionButton0 = (self.screenHeight / 90) * 10 #de height postie invoegen in de array
        self.y_postionButton1 = (self.screenHeight / 90) * 20 #^ 
        self.y_postionButton2 = (self.screenHeight / 90) * 30 #^
        self.y_postionButton3 = (self.screenHeight / 90) * 40 #^
        self.y_postionButton4 = (self.screenHeight / 90) * 50 #^
        self.y_postionButton5 = (self.screenHeight / 90) * 60 #^
        textSize = 20
        #instances
        self.menuButton0 = self.Button(self.colorDarkBlue, self.colorBlue,self.colorWhite, self.colorWhite,textSize,self.gameDisplay,self.menuButtonWidth,self.menuButtonHeight,self.x_postionButton,self.y_postionButton0, 'Start Game')
        self.menuButton1 = self.Button(self.colorDarkBlue, self.colorBlue,self.colorWhite, self.colorWhite,textSize,self.gameDisplay,self.menuButtonWidth,self.menuButtonHeight,self.x_postionButton,self.y_postionButton1, 'Load Game')
        self.menuButton2 = self.Button(self.colorDarkBlue, self.colorBlue,self.colorWhite, self.colorWhite,textSize,self.gameDisplay,self.menuButtonWidth,self.menuButtonHeight,self.x_postionButton,self.y_postionButton2, 'Settings')
        self.menuButton3 = self.Button(self.colorDarkBlue, self.colorBlue,self.colorWhite, self.colorWhite,textSize,self.gameDisplay,self.menuButtonWidth,self.menuButtonHeight,self.x_postionButton,self.y_postionButton3, 'Scorebord')
        self.menuButton4 = self.Button(self.colorDarkBlue, self.colorBlue,self.colorWhite, self.colorWhite,textSize,self.gameDisplay,self.menuButtonWidth,self.menuButtonHeight,self.x_postionButton,self.y_postionButton4, 'Game rules')
        self.menuButton5 = self.Button(self.colorDarkBlue, self.colorBlue,self.colorWhite, self.colorWhite,textSize,self.gameDisplay,self.menuButtonWidth,self.menuButtonHeight,self.x_postionButton,self.y_postionButton5, 'Quit game')
        #INSTANCE voor de hover functies!
        self.scoreboard = Scoreboard.Scoreboard(self.gameDisplay,self.screenWidth,self.screenHeight)
        self.SettingScreen = SetttingScreen.SettingScreen(self.gameDisplay,self.screenWidth,self.screenHeight,self.gameSettings)
        #Instance for music
        self.music = Music.Music('menu')
        #gamerules
        self.gameRules = GameRules.GameRules(self.screenWidth, self.screenHeight, self.gameDisplay)
        #database
        self.database = Database.Connect()
    #exit game, kan beter?
    def GameExit(self):
        return False
    #code die gerun worden tijdens het Menu
    def ShowMenu(self):
        #background
        self.gameDisplay.blit(self.backgroundImage, (0, 0))
        #roept de method aan die events regelt
        self.MenuButtonsHandler()
    #teken buttons Note: opruiming kan beter
    def MenuButtonsHandler(self):
        #valideer of een button is geklikt
        for events in pygame.event.get():
            xMousePos, yMousePos = pygame.mouse.get_pos()
            if events.type == pygame.MOUSEBUTTONUP:
                if xMousePos > self.x_postionButton and yMousePos > self.y_postionButton0 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton0 + self.menuButtonHeight):
                    self.gameScreenCurrentState = self.gameScreenStates[1]
                elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton1 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton1 + self.menuButtonHeight):
                    self.gameScreenCurrentState = self.gameScreenStates[2]
                elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton2 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton2 + self.menuButtonHeight):
                    self.gameScreenCurrentState = self.gameScreenStates[3]
                elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton3 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton3 + self.menuButtonHeight):
                    self.gameScreenCurrentState = self.gameScreenStates[4]
                elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton4 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton4 + self.menuButtonHeight):
                    self.gameScreenCurrentState = self.gameScreenStates[5]
                elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton5 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton5 + self.menuButtonHeight):
                    self.gameScreenCurrentState = self.gameScreenStates[6]
            if xMousePos > self.x_postionButton and yMousePos > self.y_postionButton0 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton0 + self.menuButtonHeight):
                self.menuButton0.ChangeColor()
            elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton1 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton1 + self.menuButtonHeight):
                self.menuButton1.ChangeColor()
            elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton2 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton2 + self.menuButtonHeight):
                self.menuButton2.ChangeColor()  
            elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton3 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton3 + self.menuButtonHeight):
                self.menuButton3.ChangeColor()
            elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton4 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton4 + self.menuButtonHeight):
                self.menuButton4.ChangeColor()
            elif xMousePos > self.x_postionButton and yMousePos > self.y_postionButton5 and xMousePos < (self.x_postionButton + self.menuButtonWidth) and yMousePos < (self.y_postionButton5 + self.menuButtonHeight):
                self.menuButton5.ChangeColor()
            else: 
                 self.menuButton0.ChangeColorBack() 
                 self.menuButton1.ChangeColorBack()
                 self.menuButton2.ChangeColorBack()   
                 self.menuButton3.ChangeColorBack()   
                 self.menuButton4.ChangeColorBack()
                 self.menuButton5.ChangeColorBack()
            if events.type == pygame.QUIT: #wil die stopen... dan stoppen we
                 self.gameScreenCurrentState = self.gameScreenStates[6] #5 = quit game = break loop
         #de postitie en de tekst voor alle buttons
        self.menuButton0.drawButtonWithLayer()
        self.menuButton1.drawButtonWithLayer()
        self.menuButton2.drawButtonWithLayer()
        self.menuButton3.drawButtonWithLayer()
        self.menuButton4.drawButtonWithLayer()
        self.menuButton5.drawButtonWithLayer()
    def StartGame(self):
        self.music.stopMusic()
        game = Game.Game(self.gameDisplay,self.screenWidth,self.screenHeight,self.gameSettings)
        game.RunGame()
        self.gameScreenCurrentState = self.gameScreenStates[0] #de RunGame is een loop, die pas wordt gebroken als de game is gestopt of afgelopen is
    def LoadGame(self):
        self.music.stopMusic()
        loadGame = Game.Game(self.gameDisplay, self.screenWidth, self.screenHeight, self.gameSettings)
        loadGame.LoadGame(self.database.SelectLoadGame(), self.database.SelectLoadGamePlayers())
        loadGame.RunGame()
        self.gameScreenCurrentState = self.gameScreenStates[0]
    def ShowSettings(self):
        self.SettingScreen.ShowSettings()
        if self.SettingScreen.EventHandler():
            self.gameScreenCurrentState = self.gameScreenStates[0]
        self.gameSettings = self.SettingScreen.gameSettings
    def ShowScoreBoard(self):
        self.scoreboard.ShowScoreBoard()
        if self.scoreboard.ExitScoreboardScreen():
            self.gameScreenCurrentState = self.gameScreenStates[0]
    def ShowGameRules(self):
        self.gameRules.showGameRules()
        if self.gameRules.ExitGameRulesScreen():
            self.gameScreenCurrentState = self.gameScreenStates[0]
    def PlayMusicInGame(self):
            self.music.playMusic(self.gameSettings['musicOn'])
    def GameLoop(self):
        while not self.GameExit():
            self.PlayMusicInGame()
            if self.gameScreenCurrentState == self.gameScreenStates[0]:
                self.ShowMenu()
            elif self.gameScreenCurrentState == self.gameScreenStates[1]:
                self.StartGame()
            elif self.gameScreenCurrentState == self.gameScreenStates[2]:
                self.LoadGame()
            elif self.gameScreenCurrentState == self.gameScreenStates[3]:
                self.ShowSettings()
            elif self.gameScreenCurrentState == self.gameScreenStates[4]:
                self.ShowScoreBoard()
            elif self.gameScreenCurrentState == self.gameScreenStates[5]:
                self.ShowGameRules()
            elif self.gameScreenCurrentState == self.gameScreenStates[6]:
                break #break the loop (dus om te exit knop te laten werken)
            else:
               self.gameScreenCurrentState == self.gameScreenStates[0] #onze 404 pagina
            pygame.display.update()
        pygame.quit()

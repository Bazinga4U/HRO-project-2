"""
@copyright 2017 Created by De Vijf Musketiers
@content this class makes a player instance
"""
import pygame
import random

class Player:
    def __init__(self,id,name,ComputerPlayer): #maakt een instantce voor player
        self.id = id #de id van de speler
        self.computerName = ['@Tim','@Tom','@Timmy','@Tommy'] #default computer namen (@ staat voor AI)
        self.x_post = 0 #x_post belangrijk voor animatie
        self.y_post = 0 #y_post belangrijk voor animatie
        self.postionName = "" #belangrijke om de positie naam op te halen
        self.pawn = Player.GetPawn(id) #afbeelding van de pawn
        if not ComputerPlayer: #zet indien nodig de computer speler naam of 'human' speler naam
            self.name = name 
        else:
            self.name = self.computerName[random.randint(0,3)] #random de naam, dus er kunnen 2x een Timmy zijn
        self.category = None #dit kan None of zelfs weg(er staat wel een verwijzing na, maar wordt niet echt gebruikt? Weet het niet zeker)
        self.newPostionName = False #volgens mij wordt deze ook niet gebruikt. Weer weet ik het niet zeker
        self.isComputerPlayer = ComputerPlayer #boolean
    def GetPawn(id):
        return pygame.image.load('img/pawns/pawn' + str(id)+ '.png')
    def SetStartPostion(self,category): #wordt niet gebruikt?
        self.category = category
    def GetPostion(self): #wordt niet gebruikt?
        return self.x_post,self.y_post
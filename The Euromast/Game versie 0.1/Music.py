"""
@copyright 2017 Created by De Vijf Musketiers
@content a class that plays the music.
"""

import pygame

pygame.init()

class Music:
    def __init__(self,music):
        self.music = music
        self.musicStarted =False
    def playMusic(self,musicOn):
        if musicOn:
            if self.musicStarted  == False:
                self.musicStarted = True
                if self.music == "menu":
                    pygame.mixer.music.load('music/main_menu.ogg')
                    pygame.mixer.music.play(-1, 0.0)
                elif self.music == "game":
                    #pygame.mixer.music.load('music/main_menu.ogg')
                    #pygame.mixer.music.play(-1, 0.0)
                    x = 0 #later komt fix, als we betere muziek hebben gevonden..?
                elif self.music == "winner":
                    pygame.mixer.music.load('music/winner.ogg')
                    pygame.mixer.music.play(-1, 0.0)
                elif self.music == "dice":
                    pygame.mixer.music.load('music/dice.ogg')
                    pygame.mixer.music.play(0, 0.0)
        else:
            self.stopMusic()

    def stopMusic(self):
        pygame.mixer.music.stop()
        self.musicStarted =False
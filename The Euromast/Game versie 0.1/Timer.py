"""
@copyright Create by De Vijf Musketiers
@content this class give a timer when needed
"""
import pygame
import time

class Timer:
    def __init__(self,boardGame):
        self.boardGame = boardGame
        self.timer = 0
        self.timerStarted = False
        self.RunOutOfTime = False
        self.timeOutAtSec = 0
        self.seconds = 0
    def StartTimer(self,seconds):
        self.timer = pygame.time.get_ticks() 
        self.timerStarted = True
        self.timeOutAtSec = seconds
        self.seconds = seconds
    def CheckTimer(self):
         seconds = (pygame.time.get_ticks()-self.timer)/1000
         self.seconds = int(self.timeOutAtSec - seconds)
         if seconds > self.timeOutAtSec:
             self.RunOutOfTime = True
    def StopTimer(self):
        self.timerStarted = False
    def RunOutOfTime(self):
        self.RunOutOfTime = True
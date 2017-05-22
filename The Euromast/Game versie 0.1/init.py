"""
@copyright 2017 Created by De Vijf Musketiers
@content the initialize of the game
"""
import pygame
import Controller

pygame.init() #init alle pygame code?

game = Controller.Controller() #instance games
game.GameLoop() #game loops
quit() #overbodig?

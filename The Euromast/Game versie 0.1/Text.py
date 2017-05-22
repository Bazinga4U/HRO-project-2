"""
@copyright Create by De Vijf Musketiers
@content a class that makes the boardgame including the functionality
"""
import pygame


class Text:
    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

    def DrawText(self, text, x_position, y_position, buttonTextColor,size):
        # vaststellen font
        myfont = pygame.font.SysFont("monoscape", size)


        # weergeeft text
        label = myfont.render(text, 1, buttonTextColor)
        self.gameDisplay.blit(label, (x_position, y_position))

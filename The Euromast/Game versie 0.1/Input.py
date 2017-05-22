"""
@copyright 2017 Created by De Vijf Musketiers
@content this class will update a "input" field
""" 
import pygame

class Input:
    #maakt een lege instance aan. Met daarin een string en kijken of of geshifted is
    def __init__(self):
        self.value = ""
        self.shifted = False
        self.maxlength = 25
        self.mouseOver = False
    #check of de string leeg is
    def IsEmpty(self):
        print(len(self.value))
        if len(self.value) == 0:
            return True
        else:
            return False
    #update de string
    def updateString(self,event):
        if self.mouseOver:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: self.shifted = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: self.value = self.value[:-1] #verwijder e.v.t. een character 
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: self.shifted = True #zet shift na true indien nodig
                elif event.key == pygame.K_SPACE: self.value += ' ' #regel spaties
                if not self.shifted:
                    if event.key == pygame.K_a: self.value += 'a'
                    elif event.key == pygame.K_b: self.value += 'b'
                    elif event.key == pygame.K_c: self.value += 'c'
                    elif event.key == pygame.K_d: self.value += 'd'
                    elif event.key == pygame.K_e: self.value += 'e'
                    elif event.key == pygame.K_f: self.value += 'f'
                    elif event.key == pygame.K_g: self.value += 'g'
                    elif event.key == pygame.K_h: self.value += 'h'
                    elif event.key == pygame.K_i: self.value += 'i'
                    elif event.key == pygame.K_j: self.value += 'j'
                    elif event.key == pygame.K_k: self.value += 'k'
                    elif event.key == pygame.K_l: self.value += 'l'
                    elif event.key == pygame.K_m: self.value += 'm'
                    elif event.key == pygame.K_n: self.value += 'n'
                    elif event.key == pygame.K_o: self.value += 'o'
                    elif event.key == pygame.K_p: self.value += 'p'
                    elif event.key == pygame.K_q: self.value += 'q'
                    elif event.key == pygame.K_r: self.value += 'r'
                    elif event.key == pygame.K_s: self.value += 's'
                    elif event.key == pygame.K_t: self.value += 't'
                    elif event.key == pygame.K_u: self.value += 'u'
                    elif event.key == pygame.K_v: self.value += 'v'
                    elif event.key == pygame.K_w: self.value += 'w'
                    elif event.key == pygame.K_x: self.value += 'x'
                    elif event.key == pygame.K_y: self.value += 'y'
                    elif event.key == pygame.K_z: self.value += 'z'
                    elif event.key == pygame.K_0: self.value += '0'
                    elif event.key == pygame.K_1: self.value += '1'
                    elif event.key == pygame.K_2: self.value += '2'
                    elif event.key == pygame.K_3: self.value += '3'
                    elif event.key == pygame.K_4: self.value += '4'
                    elif event.key == pygame.K_5: self.value += '5'
                    elif event.key == pygame.K_6: self.value += '6'
                    elif event.key == pygame.K_7: self.value += '7'
                    elif event.key == pygame.K_8: self.value += '8'
                    elif event.key == pygame.K_9: self.value += '9'
                elif self.shifted:
                    if event.key == pygame.K_a: self.value += 'A'
                    elif event.key == pygame.K_b: self.value += 'B'
                    elif event.key == pygame.K_c: self.value += 'C'
                    elif event.key == pygame.K_d: self.value += 'D'
                    elif event.key == pygame.K_e: self.value += 'E'
                    elif event.key == pygame.K_f: self.value += 'F'
                    elif event.key == pygame.K_g: self.value += 'G'
                    elif event.key == pygame.K_h: self.value += 'H'
                    elif event.key == pygame.K_i: self.value += 'I'
                    elif event.key == pygame.K_j: self.value += 'J'
                    elif event.key == pygame.K_k: self.value += 'K'
                    elif event.key == pygame.K_l: self.value += 'L'
                    elif event.key == pygame.K_m: self.value += 'M'
                    elif event.key == pygame.K_n: self.value += 'N'
                    elif event.key == pygame.K_o: self.value += 'O'
                    elif event.key == pygame.K_p: self.value += 'P'
                    elif event.key == pygame.K_q: self.value += 'Q'
                    elif event.key == pygame.K_r: self.value += 'R'
                    elif event.key == pygame.K_s: self.value += 'S'
                    elif event.key == pygame.K_t: self.value += 'T'
                    elif event.key == pygame.K_u: self.value += 'U'
                    elif event.key == pygame.K_v: self.value += 'V'
                    elif event.key == pygame.K_w: self.value += 'W'
                    elif event.key == pygame.K_x: self.value += 'X'
                    elif event.key == pygame.K_y: self.value += 'Y'
                    elif event.key == pygame.K_z: self.value += 'Z'
            if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]
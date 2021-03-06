#Natalie Lunbeck
#CS269: Game Design
#Shadow Puppets

#This class creates a block object for platforms
import pygame
import os
import sys
from pygame.locals import *
from lighting import *
from Letters import *
from Door import *

bg = pygame.image.load('Assets/CaveContrast.png')
b1 = pygame.image.load('Assets/block1.png')
b2 = pygame.image.load('Assets/block2.png')
b3 = pygame.image.load('Assets/block3.png')
b4 = pygame.image.load('Assets/block4.png')

class Block(pygame.sprite.Sprite):
    #block code that tells the program what type of block this will be
    #0 = platform, 1 = wall
    block_type = 0
    
    def __init__(self, x_pos, y_pos, width, height, sprite):
        #creating a new block
        pygame.sprite.Sprite.__init__(self)
        if sprite == "block1.png":
            self.image = b1
        elif sprite == "block2.png":
            self.image = b2
        elif sprite == "block3.png":
            self.image = b3
        elif sprite == "block4.png":
        	self.image = b4
        else:
            self.image = b1
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        #loading a sprite in and giving it a transparent background
        #self.image.convert_alpha()
        #self.image = pygame.Surface((width, height))
        #self.image.fill((0,0,255))
        #self.image.set_colorkey()
        #giving a rigidbody
        self.rect = self.image.get_rect()
        #setting coordinates
        self.rect.centerx = x_pos
        self.rect.y = y_pos
        new_height = height - 2
        #makes the rect 2 px high
        self.rect.inflate(0, -40)
        #print(self.rect)
        #block defaults to platform
        if sprite != "block4.png":
            self.collisionRect = pygame.Rect((self.rect.left, self.rect.top), (self.rect.width, self.rect.height/2))
        else:
            self.collisionRect = self.rect
        
    def getX(self):
        return self.rect.x
    
    def getY(self): 
        return self.rect.y
    
    def setX(new_x):
        self.rect.x = new_x
        
    def setY(new_y):
        self.rect.y = new_y
        
    def setBlock(num):
        #change block to either a platform or wall
        if num != 0:
            self.block_type = 1
        else:
            self.block_type = 0
            

def layout_level1(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    platforms = []
    ar_x = 1.3
    ar_y = 1.5

    platforms.append(Block(50,490, p_width, p_height, "block1.png"))
    platforms.append(Block(150,490, p_width, p_height, "block1.png"))
    platforms.append(Block(250,490, p_width, p_height, "block1.png"))
    platforms.append(Block(350,490, p_width, p_height, "block1.png"))
    platforms.append(Block(450,490, p_width, p_height, "block1.png"))
    platforms.append(Block(550,490, p_width, p_height, "block1.png"))
    platforms.append(Block(650,490, p_width, p_height, "block1.png"))
    platforms.append(Block(750,490, p_width, p_height, "block1.png"))
    
    lampHeight = lampImage.get_height()
    
    lampList = [Lamp( (750, 490), lampImage, lightAlpha, 10 )]
    
    doorList = [Door( (50, 490), False), Door( (650, 490), True)]
    
    return platforms, lampList, doorList

def layout_level2(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    platforms = []
    ar_x = 1.3
    ar_y = 1.5
    
    platforms.append(Block(50,490, p_width, p_height, "block1.png"))
    platforms.append(Block(150,490, p_width, p_height, "block1.png"))
    platforms.append(Block(250,490, p_width, p_height, "block1.png"))
    platforms.append(Block(350,490, p_width, p_height, "block1.png"))
    platforms.append(Block(450,490, p_width, p_height, "block1.png"))
    platforms.append(Block(550,490, p_width, p_height, "block1.png"))
    platforms.append(Block(650,490, p_width, p_height, "block1.png"))
    platforms.append(Block(750,490, p_width, p_height, "block1.png"))
    
    platforms.append(Block(450,385, p_width, p_height, "block1.png"))
    
    lampHeight = lampImage.get_height()
    
    lampList = [Lamp( (450, 385), lampImage, lightAlpha, 10 ), Lamp( (650, 490), lampImage, lightAlpha, isLit = True )]
    
    doorList = [Door( (50, 490), False), Door( (750, 490), True)]
    
    return platforms, lampList, doorList
    

def layout_level3(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    platforms = []
    ar_x = 1.3
    ar_y = 1.5
    
    platforms.append(Block(50,490, p_width, p_height, "block1.png"))
    platforms.append(Block(150,490, p_width, p_height, "block1.png"))
    platforms.append(Block(250,490, p_width, p_height, "block1.png"))
    platforms.append(Block(350,490, p_width, p_height, "block1.png"))
    platforms.append(Block(450,490, p_width, p_height, "block1.png"))
    platforms.append(Block(550,490, p_width, p_height, "block1.png"))
    platforms.append(Block(650,490, p_width, p_height, "block1.png"))
    platforms.append(Block(750,490, p_width, p_height, "block1.png"))

    
    lampHeight = lampImage.get_height()
    
    lampList = [Lamp( (250, 490), lampImage, lightAlpha, 1 ), Lamp( (650, 490), lampImage, lightAlpha, 5 )]
    
    doorList = [Door( (50, 490), False), Door( (750, 490), True)]
    
    return platforms, lampList, doorList
    
def layout_level4(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    p4_height = 105
    p4_width = 15
    
    platforms = []
    
    
    platforms.append(Block(150,70, p_width, p_height, "block1.png"))
    platforms.append(Block(550,70, p_width, p_height, "block1.png"))
    platforms.append(Block(650,175, p_width, p_height, "block1.png"))
    platforms.append(Block(250,280, p_width, p_height, "block1.png"))
    platforms.append(Block(650,280, p_width, p_height, "block1.png"))
    platforms.append(Block(50,385, p_width, p_height, "block1.png"))
    platforms.append(Block(650,385, p_width, p_height, "block1.png"))
    platforms.append(Block(50,490, p_width, p_height, "block1.png"))
    platforms.append(Block(150,490, p_width, p_height, "block1.png"))
    platforms.append(Block(450,490, p_width, p_height, "block1.png"))
    platforms.append(Block(750,490, p_width, p_height, "block1.png"))
    
    platforms.append(Block(250,70, p_width, p_height, "block2.png"))
    platforms.append(Block(50,175, p_width, p_height, "block2.png"))
    platforms.append(Block(250,175, p_width, p_height, "block2.png"))
    platforms.append(Block(450,175, p_width, p_height, "block2.png"))
    platforms.append(Block(550,175, p_width, p_height, "block2.png"))
    platforms.append(Block(150,280, p_width, p_height, "block2.png"))
    platforms.append(Block(550,280, p_width, p_height, "block2.png"))
    platforms.append(Block(250,385, p_width, p_height, "block2.png"))
    platforms.append(Block(650,490, p_width, p_height, "block2.png"))
    
    platforms.append(Block(775,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(325,385, p3_width, p_height, "block3.png"))
    platforms.append(Block(225,490, p3_width, p_height, "block3.png"))
    
    #Floor
    platforms.append(Block(50,590, p_width, p_height, "block1.png"))
    platforms.append(Block(150,590, p_width, p_height, "block1.png"))
    platforms.append(Block(250,590, p_width, p_height, "block1.png"))
    platforms.append(Block(350,590, p_width, p_height, "block1.png"))
    platforms.append(Block(450,590, p_width, p_height, "block1.png"))
    platforms.append(Block(550,590, p_width, p_height, "block1.png"))
    platforms.append(Block(650,590, p_width, p_height, "block1.png"))
    platforms.append(Block(750,590, p_width, p_height, "block1.png"))
    
    lampHeight = lampImage.get_height()
    
    lampList = [ Lamp( (150, 490), lampImage, lightAlpha, isLit = True ), Lamp( (250,70), lampImage, lightAlpha, 10 ), Lamp( (650,385), lampImage, lightAlpha, 5 ) ]
    
    doorList = [Door( (750, 490), False), Door( (50, 490), True)]
    
    return platforms, lampList, doorList, None

def layout_level5(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    p4_height = 105
    p4_width = 15
    
    platforms = []
    
    
    platforms.append(Block(50,70, p_width, p_height, "block1.png"))
    platforms.append(Block(750,70, p_width, p_height, "block1.png"))
    platforms.append(Block(250,175, p_width, p_height, "block1.png"))
    platforms.append(Block(650,175, p_width, p_height, "block1.png"))
    platforms.append(Block(50,280, p_width, p_height, "block1.png"))
    platforms.append(Block(350,280, p_width, p_height, "block1.png"))
    platforms.append(Block(50,385, p_width, p_height, "block1.png"))
    platforms.append(Block(350,385, p_width, p_height, "block1.png"))
    platforms.append(Block(750,385, p_width, p_height, "block1.png"))
    platforms.append(Block(550,490, p_width, p_height, "block1.png"))
    
    platforms.append(Block(150,70, p_width, p_height, "block2.png"))
    platforms.append(Block(650,70, p_width, p_height, "block2.png"))
    platforms.append(Block(350,175, p_width, p_height, "block2.png"))
    platforms.append(Block(550,175, p_width, p_height, "block2.png"))
    platforms.append(Block(150,280, p_width, p_height, "block2.png"))
    platforms.append(Block(250,280, p_width, p_height, "block2.png"))
    platforms.append(Block(750,280, p_width, p_height, "block2.png"))
    platforms.append(Block(650,385, p_width, p_height, "block2.png"))
    platforms.append(Block(450,385, p_width, p_height, "block2.png"))
    platforms.append(Block(50,490, p_width, p_height, "block2.png"))
    platforms.append(Block(550,175, p_width, p_height, "block2.png"))
    platforms.append(Block(150,490, p_width, p_height, "block2.png"))
    platforms.append(Block(450,490, p_width, p_height, "block2.png"))
    platforms.append(Block(650,490, p_width, p_height, "block2.png"))
    platforms.append(Block(750,490, p_width, p_height, "block2.png"))
    
    platforms.append(Block(225,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(175,175, p3_width, p_height, "block3.png"))
    platforms.append(Block(725,175, p3_width, p_height, "block3.png"))
    platforms.append(Block(675,280, p3_width, p_height, "block3.png"))
    platforms.append(Block(225,490, p3_width, p_height, "block3.png"))
    platforms.append(Block(375,490, p3_width, p_height, "block3.png"))
    
    # Walls
    platforms.append(Block(310,175, p4_width, p4_height, "block4.png"))
    platforms.append(Block(400,385, p4_width, p4_height, "block4.png"))
    
    #Floor
    platforms.append(Block(50,590, p_width, p_height, "block1.png"))
    platforms.append(Block(150,590, p_width, p_height, "block1.png"))
    platforms.append(Block(250,590, p_width, p_height, "block1.png"))
    platforms.append(Block(350,590, p_width, p_height, "block1.png"))
    platforms.append(Block(450,590, p_width, p_height, "block1.png"))
    platforms.append(Block(550,590, p_width, p_height, "block1.png"))
    platforms.append(Block(650,590, p_width, p_height, "block1.png"))
    platforms.append(Block(750,590, p_width, p_height, "block1.png"))
    
    lampHeight = lampImage.get_height()
    
    lampList = [ Lamp( (150, 70), lampImage, lightAlpha, 15 ), Lamp( (650,70), lampImage, lightAlpha, 15 ), Lamp( (150,490), lampImage, lightAlpha, 10 ), Lamp( (650,490), lampImage, lightAlpha, 15 ) ]
    
    letter = Letter( pygame.image.load('Assets/Letters/letter1.png'), (450,385) )
    
    doorList = [Door( (50, 70), False), Door( (750, 490), True)]
    
    return platforms, lampList, doorList, letter

def layout_level6(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    p4_height = 105
    p4_width = 15
    
    platforms = []
    
    
    platforms.append(Block(750,175, p_width, p_height, "block1.png"))
    platforms.append(Block(150,280, p_width, p_height, "block1.png"))
    platforms.append(Block(550,280, p_width, p_height, "block1.png"))
    platforms.append(Block(350,385, p_width, p_height, "block1.png"))
    platforms.append(Block(250,490, p_width, p_height, "block1.png"))
    platforms.append(Block(650,490, p_width, p_height, "block1.png"))
    
    platforms.append(Block(350,175, p_width, p_height, "block2.png"))
    platforms.append(Block(550,175, p_width, p_height, "block2.png"))
    platforms.append(Block(250,280, p_width, p_height, "block2.png"))
    platforms.append(Block(450,280, p_width, p_height, "block2.png"))
    platforms.append(Block(650,280, p_width, p_height, "block2.png"))
    platforms.append(Block(150,385, p_width, p_height, "block2.png"))
    platforms.append(Block(550,385, p_width, p_height, "block2.png"))
    platforms.append(Block(50,490, p_width, p_height, "block2.png"))
    platforms.append(Block(350,490, p_width, p_height, "block2.png"))
    platforms.append(Block(450,490, p_width, p_height, "block2.png"))
    
    platforms.append(Block(125,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(375,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(575,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(725,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(75,280, p3_width, p_height, "block3.png"))
    platforms.append(Block(725,490, p3_width, p_height, "block3.png"))
    
    # Walls
    platforms.append(Block(300,175, p4_width, p4_height, "block4.png"))
    platforms.append(Block(710,70, p4_width, p4_height, "block4.png"))
    platforms.append(Block(200,280, p4_width, p4_height, "block4.png"))
    platforms.append(Block(510,280, p4_width, p4_height, "block4.png"))
    platforms.append(Block(400,385, p4_width, p4_height, "block4.png"))
    platforms.append(Block(700,385, p4_width, p4_height, "block4.png"))
    platforms.append(Block(310,490, p4_width, p4_height, "block4.png"))
    
    #Floor
    platforms.append(Block(50,590, p_width, p_height, "block1.png"))
    platforms.append(Block(150,590, p_width, p_height, "block1.png"))
    platforms.append(Block(250,590, p_width, p_height, "block1.png"))
    platforms.append(Block(350,590, p_width, p_height, "block1.png"))
    platforms.append(Block(450,590, p_width, p_height, "block1.png"))
    platforms.append(Block(550,590, p_width, p_height, "block1.png"))
    platforms.append(Block(650,590, p_width, p_height, "block1.png"))
    platforms.append(Block(750,590, p_width, p_height, "block1.png"))
    
    lampHeight = lampImage.get_height()
    
    lampList = [ Lamp( (575, 70), lampImage, lightAlpha, 15 ), Lamp( (250,280), lampImage, lightAlpha, 10 ), Lamp( (250,490), lampImage, lightAlpha, 20 ) ]
    
    letter = Letter( pygame.image.load('Assets/Letters/letter2.png'), (125,70) )
    
    doorList = [Door( (50, 490), False), Door( (350, 490), True)]
    
    return platforms, lampList, doorList, letter

def layout_level7(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    p4_height = 105
    p4_width = 15
    
    platforms = []
    
    
    platforms.append(Block(50,70, p_width, p_height, "block1.png"))
    platforms.append(Block(150,175, p_width, p_height, "block1.png"))
    platforms.append(Block(350,175, p_width, p_height, "block1.png"))
    platforms.append(Block(650,175, p_width, p_height, "block1.png"))
    platforms.append(Block(50,280, p_width, p_height, "block1.png"))
    platforms.append(Block(450,280, p_width, p_height, "block1.png"))
    platforms.append(Block(750,280, p_width, p_height, "block1.png"))
    platforms.append(Block(50,385, p_width, p_height, "block1.png"))
    platforms.append(Block(350,385, p_width, p_height, "block1.png"))
    platforms.append(Block(650,385, p_width, p_height, "block1.png"))
    platforms.append(Block(150,490, p_width, p_height, "block1.png"))
    platforms.append(Block(550,490, p_width, p_height, "block1.png"))
    
    platforms.append(Block(150,70, p_width, p_height, "block2.png"))
    platforms.append(Block(350,70, p_width, p_height, "block2.png"))
    platforms.append(Block(450,70, p_width, p_height, "block2.png"))
    platforms.append(Block(650,70, p_width, p_height, "block2.png"))
    platforms.append(Block(250,175, p_width, p_height, "block2.png"))
    platforms.append(Block(550,175, p_width, p_height, "block2.png"))
    platforms.append(Block(750,175, p_width, p_height, "block2.png"))
    platforms.append(Block(150,280, p_width, p_height, "block2.png"))
    platforms.append(Block(350,280, p_width, p_height, "block2.png"))
    platforms.append(Block(150,385, p_width, p_height, "block2.png"))
    platforms.append(Block(550,385, p_width, p_height, "block2.png"))
    platforms.append(Block(750,490, p_width, p_height, "block2.png"))
    
    platforms.append(Block(525,280, p3_width, p_height, "block3.png"))
    platforms.append(Block(225,385, p3_width, p_height, "block3.png"))
    platforms.append(Block(725,385, p3_width, p_height, "block3.png"))
    platforms.append(Block(225,490, p3_width, p_height, "block3.png"))
    platforms.append(Block(475,490, p3_width, p_height, "block3.png"))
    
    # Walls
    platforms.append(Block(190,175, p4_width, p4_height, "block4.png"))
    platforms.append(Block(510,280, p4_width, p4_height, "block4.png"))
    platforms.append(Block(200,385, p4_width, p4_height, "block4.png"))
    platforms.append(Block(500,490, p4_width, p4_height, "block4.png"))
    
    #Floor
    platforms.append(Block(50,590, p_width, p_height, "block1.png"))
    platforms.append(Block(150,590, p_width, p_height, "block1.png"))
    platforms.append(Block(250,590, p_width, p_height, "block1.png"))
    platforms.append(Block(350,590, p_width, p_height, "block1.png"))
    platforms.append(Block(450,590, p_width, p_height, "block1.png"))
    platforms.append(Block(550,590, p_width, p_height, "block1.png"))
    platforms.append(Block(650,590, p_width, p_height, "block1.png"))
    platforms.append(Block(750,590, p_width, p_height, "block1.png"))
    
    lampHeight = lampImage.get_height()
    
    lampList = [ Lamp( (650, 175), lampImage, lightAlpha, 15 ), Lamp( (150,280), lampImage, lightAlpha, 10 ), Lamp( (150,490), lampImage, lightAlpha, 20 ) ]
    
    letter = Letter( pygame.image.load('Assets/Letters/letter3.png'), (750,280) )
    
    doorList = [Door( (750, 490), False), Door( (50, 70), True)]
    
    
    return platforms, lampList, doorList, letter
    
def layout_level8(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    p4_height = 105
    p4_width = 15
    
    platforms = []
    
    
    platforms.append(Block(50,70, p_width, p_height, "block1.png"))
    platforms.append(Block(250,70, p_width, p_height, "block1.png"))
    platforms.append(Block(550,70, p_width, p_height, "block1.png"))
    platforms.append(Block(50,175, p_width, p_height, "block1.png"))
    platforms.append(Block(750,175, p_width, p_height, "block1.png"))
    platforms.append(Block(150,280, p_width, p_height, "block1.png"))
    platforms.append(Block(550,280, p_width, p_height, "block1.png"))
    platforms.append(Block(250,490, p_width, p_height, "block1.png"))
    platforms.append(Block(550,490, p_width, p_height, "block1.png"))
    platforms.append(Block(650,70, p_width, p_height, "block1.png"))
    
    platforms.append(Block(150,70, p_width, p_height, "block2.png"))
    platforms.append(Block(350,70, p_width, p_height, "block2.png"))
    platforms.append(Block(650,175, p_width, p_height, "block2.png"))
    platforms.append(Block(250,280, p_width, p_height, "block2.png"))
    platforms.append(Block(650,280, p_width, p_height, "block2.png"))
    platforms.append(Block(50,385, p_width, p_height, "block2.png"))
    platforms.append(Block(650,385, p_width, p_height, "block2.png"))
    platforms.append(Block(150,490, p_width, p_height, "block2.png"))
    platforms.append(Block(450,490, p_width, p_height, "block2.png"))
    platforms.append(Block(450,385, p_width, p_height, "block2.png"))
    
    platforms.append(Block(775,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(225,175, p3_width, p_height, "block3.png"))
    platforms.append(Block(775,280, p3_width, p_height, "block3.png"))
    platforms.append(Block(225,385, p3_width, p_height, "block3.png"))
    platforms.append(Block(725,385, p3_width, p_height, "block3.png"))
    platforms.append(Block(775,490, p3_width, p_height, "block3.png"))
    
    # Walls
    platforms.append(Block(700,0, p4_width, p4_height, "block4.png"))
    platforms.append(Block(200,70, p4_width, p4_height, "block4.png"))
    platforms.append(Block(200,175, p4_width, p4_height, "block4.png"))
    platforms.append(Block(400,175, p4_width, p4_height, "block4.png"))
    platforms.append(Block(690,175, p4_width, p4_height, "block4.png"))
    platforms.append(Block(200,385, p4_width, p4_height, "block4.png"))
    platforms.append(Block(700,385, p4_width, p4_height, "block4.png"))
    platforms.append(Block(200,490, p4_width, p4_height, "block4.png"))
    platforms.append(Block(400,490, p4_width, p4_height, "block4.png"))
    
    #Floor
    platforms.append(Block(50,590, p_width, p_height, "block1.png"))
    platforms.append(Block(150,590, p_width, p_height, "block1.png"))
    platforms.append(Block(250,590, p_width, p_height, "block1.png"))
    platforms.append(Block(350,590, p_width, p_height, "block1.png"))
    platforms.append(Block(450,590, p_width, p_height, "block1.png"))
    platforms.append(Block(550,590, p_width, p_height, "block1.png"))
    platforms.append(Block(650,590, p_width, p_height, "block1.png"))
    platforms.append(Block(750,590, p_width, p_height, "block1.png"))
    
    lampHeight = lampImage.get_height()
    
    lampList = [ Lamp( ( 50, 175), lampImage, lightAlpha, 25 ), Lamp( (775,70), lampImage, lightAlpha, 15 ), Lamp( (775,280), lampImage, lightAlpha, 10 ), Lamp( (650,590), lampImage, lightAlpha, 5 ) ]
    
    letter = Letter( pygame.image.load('Assets/Letters/letter4.png'), (200,385) )
    
    doorList = [Door( (50, 70), False), Door( (720, 590), True)]
    
    
    return platforms, lampList, doorList, letter
    
def layout_level9(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    p4_height = 105
    p4_width = 15
    
    platforms = []
    
    
    platforms.append(Block(450,70, p_width, p_height, "block1.png"))
    platforms.append(Block(250,175, p_width, p_height, "block1.png"))
    platforms.append(Block(450,280, p_width, p_height, "block1.png"))
    platforms.append(Block(350,385, p_width, p_height, "block1.png"))
    platforms.append(Block(50,490, p_width, p_height, "block1.png"))
    platforms.append(Block(450,490, p_width, p_height, "block1.png"))
    platforms.append(Block(250,490, p_width, p_height, "block1.png"))
    
    platforms.append(Block(50,175, p_width, p_height, "block2.png"))
    platforms.append(Block(150,280, p_width, p_height, "block2.png"))
    platforms.append(Block(750,280, p_width, p_height, "block2.png"))
    platforms.append(Block(550,385, p_width, p_height, "block2.png"))
    platforms.append(Block(550,490, p_width, p_height, "block2.png"))
    
    platforms.append(Block(125,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(625,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(775,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(375,175, p3_width, p_height, "block3.png"))
    platforms.append(Block(425,175, p3_width, p_height, "block3.png"))
    platforms.append(Block(25,280, p3_width, p_height, "block3.png"))
    platforms.append(Block(75,385, p3_width, p_height, "block3.png"))
    platforms.append(Block(175,385, p3_width, p_height, "block3.png"))
    platforms.append(Block(725,490, p3_width, p_height, "block3.png"))
    
    # Walls
    platforms.append(Block(200,70, p4_width, p4_height, "block4.png"))
    platforms.append(Block(300,70, p4_width, p4_height, "block4.png"))
    platforms.append(Block(700,70, p4_width, p4_height, "block4.png"))
    platforms.append(Block(100,175, p4_width, p4_height, "block4.png"))
    platforms.append(Block(200,175, p4_width, p4_height, "block4.png"))
    platforms.append(Block(300,280, p4_width, p4_height, "block4.png"))
    platforms.append(Block(500,280, p4_width, p4_height, "block4.png"))
    platforms.append(Block(600,280, p4_width, p4_height, "block4.png"))
    platforms.append(Block(700,385, p4_width, p4_height, "block4.png"))
    platforms.append(Block(100,385, p4_width, p4_height, "block4.png"))
    platforms.append(Block(300,490, p4_width, p4_height, "block4.png"))
    platforms.append(Block(500,490, p4_width, p4_height, "block4.png"))

    
    #Floor
    platforms.append(Block(50,590, p_width, p_height, "block1.png"))
    platforms.append(Block(150,590, p_width, p_height, "block1.png"))
    platforms.append(Block(250,590, p_width, p_height, "block1.png"))
    platforms.append(Block(350,590, p_width, p_height, "block1.png"))
    platforms.append(Block(450,590, p_width, p_height, "block1.png"))
    platforms.append(Block(550,590, p_width, p_height, "block1.png"))
    platforms.append(Block(650,590, p_width, p_height, "block1.png"))
    platforms.append(Block(750,590, p_width, p_height, "block1.png"))
    
    lampHeight = lampImage.get_height()
    
    lampList = [ Lamp( ( 25, 280), lampImage, lightAlpha, 25 ), Lamp( (50,590), lampImage, lightAlpha, 20 ), Lamp( (250,175), lampImage, lightAlpha, 10 ), Lamp( (600,590), lampImage, lightAlpha, 5 ), Lamp( (625,70), lampImage, lightAlpha, 20 ) ]
    
    letter = Letter( pygame.image.load('Assets/Letters/letter5.png'), (450,280) )
    
    doorList = [Door( (350, 590), False), Door( (550, 590), True)]
    
    
    return platforms, lampList, doorList, letter

def layout_level10(screen):
    p3_width = 50
    p_height = 50
    p_width = 100
    p4_height = 105
    p4_width = 15
    
    platforms = []
    
    
    platforms.append(Block(50,70, p_width, p_height, "block1.png"))
    platforms.append(Block(750,70, p_width, p_height, "block1.png"))
    platforms.append(Block(250,175, p_width, p_height, "block1.png"))
    platforms.append(Block(650,175, p_width, p_height, "block1.png"))
    platforms.append(Block(50,280, p_width, p_height, "block1.png"))
    platforms.append(Block(350,280, p_width, p_height, "block1.png"))
    platforms.append(Block(50,385, p_width, p_height, "block1.png"))
    platforms.append(Block(350,385, p_width, p_height, "block1.png"))
    platforms.append(Block(750,385, p_width, p_height, "block1.png"))
    platforms.append(Block(550,490, p_width, p_height, "block1.png"))
    
    platforms.append(Block(150,70, p_width, p_height, "block2.png"))
    platforms.append(Block(650,70, p_width, p_height, "block2.png"))
    platforms.append(Block(350,175, p_width, p_height, "block2.png"))
    platforms.append(Block(550,175, p_width, p_height, "block2.png"))
    platforms.append(Block(150,280, p_width, p_height, "block2.png"))
    platforms.append(Block(250,280, p_width, p_height, "block2.png"))
    platforms.append(Block(750,280, p_width, p_height, "block2.png"))
    platforms.append(Block(650,385, p_width, p_height, "block2.png"))
    platforms.append(Block(450,385, p_width, p_height, "block2.png"))
    platforms.append(Block(50,490, p_width, p_height, "block2.png"))
    platforms.append(Block(550,175, p_width, p_height, "block2.png"))
    platforms.append(Block(150,490, p_width, p_height, "block2.png"))
    platforms.append(Block(450,490, p_width, p_height, "block2.png"))
    platforms.append(Block(650,490, p_width, p_height, "block2.png"))
    platforms.append(Block(750,490, p_width, p_height, "block2.png"))
    
    platforms.append(Block(225,70, p3_width, p_height, "block3.png"))
    platforms.append(Block(175,175, p3_width, p_height, "block3.png"))
    platforms.append(Block(725,175, p3_width, p_height, "block3.png"))
    platforms.append(Block(675,280, p3_width, p_height, "block3.png"))
    platforms.append(Block(225,490, p3_width, p_height, "block3.png"))
    platforms.append(Block(375,490, p3_width, p_height, "block3.png"))
    
    # Walls
    platforms.append(Block(310,175, p4_width, p4_height, "block4.png"))
    platforms.append(Block(400,385, p4_width, p4_height, "block4.png"))
    
    #Floor
    platforms.append(Block(50,590, p_width, p_height, "block1.png"))
    platforms.append(Block(150,590, p_width, p_height, "block1.png"))
    platforms.append(Block(250,590, p_width, p_height, "block1.png"))
    platforms.append(Block(350,590, p_width, p_height, "block1.png"))
    platforms.append(Block(450,590, p_width, p_height, "block1.png"))
    platforms.append(Block(550,590, p_width, p_height, "block1.png"))
    platforms.append(Block(650,590, p_width, p_height, "block1.png"))
    platforms.append(Block(750,590, p_width, p_height, "block1.png"))
    
    lampHeight = lampImage.get_height()
    
    lampList = [ Lamp( (150, 70), lampImage, lightAlpha, 20 ), Lamp( (650,175), lampImage, lightAlpha, 20 ), Lamp( (150,490), lampImage, lightAlpha, 20 ), Lamp( (650,490), lampImage, lightAlpha, 20 ), Lamp( (350,280), lampImage, lightAlpha, 20 ) ]
    
    doorList = [Door( (50, 70), False), Door( (750, 490), True)]
    
    return platforms, lampList, doorList, None
    

class Layout():
    #dimensions are 800x600
    level = 1
    def __init__(self, cur_level, screen):
        self.level = cur_level
        if cur_level == 1:
            layout_level1(screen)
        else:
            print("level does not exist yet")

if __name__=="__main__":
    print(layout_level1())





'''
#This class creates a block object for platforms
import pygame
import os
import sys

from lighting import *

class Block(pygame.sprite.Sprite):
    #block code that tells the program what type of block this will be
    #0 = platform, 1 = wall
    block_type = 0
    
    def __init__(self, x_pos, y_pos, width, height, sprite):
        #creating a new block
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets',sprite)).convert()
        #loading a sprite in and giving it a transparent background
        self.image.convert_alpha()
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,255))
        #self.image.set_colorkey()
        #giving a rigidbody
        self.rect = self.image.get_rect()
        #setting coordinates
        self.rect.x = x_pos
        self.rect.y = y_pos
        #block defaults to platform
        
    def getX():
        return self.rect.x
    
    def getY(): 
        return self.rect.y
    
    def setX(new_x):
        self.rect.x = new_x
        
    def setY(new_y):
        self.rect.y = new_y
        
    def setBlock(num):
        #change block to either a platform or wall
        if num != 0:
            self.block_type = 1
        else:
            self.block_type = 0
            
            
def layout_level1(screen):
    #screen = pygame.display.set_mode([800,600])
    background = pygame.image.load(os.path.join('Assets','CaveContrast.png')).convert()
    edges = screen.get_rect()
    p_height = 30
    p_width = 100
    platforms = []
    
    #first row
    platforms.append(Block(4,60, p_width, p_height, "block1.png"))
    platforms.append(Block(118,60, p_width, p_height, "block2.png"))
    platforms.append(Block(480, 60, p_width, p_height, "block1.png"))
    
    #second row
    platforms.append(Block(140,140, p_width, p_height, "block1.png"))
    platforms.append(Block(417,140, p_width, p_height, "block2.png"))
    platforms.append(Block(534,140, p_width/2, p_height, "block3.png"))
    
    #third row
    platforms.append(Block(5, 215, p_width, p_height, "block2.png"))
    platforms.append(Block(136, 215, p_width, p_height, "block1.png"))
    platforms.append(Block(266, 215, p_width, p_height, "block2.png"))
    platforms.append(Block(386, 215, p_width/2, p_height, "block3.png"))
    
    #fourth row
    platforms.append(Block(2, 302, p_width, p_height, "block1.png"))
    platforms.append(Block(210, 302, p_width, p_height, "block2.png"))
    platforms.append(Block(330, 302, p_width/2, p_height, "block3.png"))
    platforms.append(Block(480, 302, p_width, p_height, "block2.png"))
    
    #fifth row
    platforms.append(Block(2, 371, p_width, p_height, "block2.png"))
    platforms.append(Block(129, 371, p_width/2, p_height, "block3.png"))
    platforms.append(Block(267, 371, p_width/2, p_height, "block3.png"))
    platforms.append(Block(342, 371, p_width, p_height, "block1.png"))
    platforms.append(Block(578, 371, p_width, p_height, "block2.png"))
    
    return platforms
    

class Layout():
    #dimensions are 800x600
    level = 1
    def __init__(self, cur_level, screen):
        self.level = cur_level
        if cur_level == 1:
            layout_level1(screen)
        else:
            print("level does not exist yet")

if __name__=="__main__":
    print(layout_level1())
'''
'''   
class Pickup():
    pickup_type = 1
    #this tells us what type of object we are creating
    #1 = key
    def __init__(self, obj_type = 1, x_pos, y_pos):
        self.pickup_type = obj_type
        self.image = pygame.Surface((20, 20))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        #setting coordinates
        self.rect.x = x_pos
        self.rect.y = y_pos
        if obj_type == 1:
            print("this is a key")
            #set sprite to key
        else:
            print("object does not exist yet")

        
'''


    
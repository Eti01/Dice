import pygame as game
import pygame
import random as r
import time as wait

icon = pygame.image.load("Dice6.png")
pygame.display.set_icon(icon)
screen = game.display.set_mode((160, 150))
screen.fill((230, 230, 230))
game.display.update()
game.display.set_caption("Dice generator")
DiceX= 26
DiceY= 35
dice = r.randrange(1,7) 

if dice == 1: 
    Dice = game.image.load('Dice1.png')
elif dice == 2:  
    Dice = game.image.load('Dice2.png')
elif dice == 3: 
    Dice = game.image.load('Dice3.png')
elif dice == 4: 
    Dice = game.image.load('Dice4.png')
elif dice == 5: 
    Dice = game.image.load('Dice5.png')
elif dice == 6: 
    Dice = game.image.load('Dice6.png')

def dice(x, y):
    screen.blit(Dice, (x, y))
dice(DiceX, DiceY)


game.display.update()
running = True
while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        if event.type == game.KEYDOWN:
            if event.key == game.K_q:
                running = False
            if event.key == game.K_r:
                dice = r.randrange(1,7) 
                if dice == 1: 
                    Dice = game.image.load('Dice1.png')
                elif dice == 2:  
                    Dice = game.image.load('Dice2.png')
                elif dice == 3: 
                    Dice = game.image.load('Dice3.png')
                elif dice == 4: 
                    Dice = game.image.load('Dice4.png')
                elif dice == 5: 
                    Dice = game.image.load('Dice5.png')
                elif dice == 6: 
                    Dice = game.image.load('Dice6.png')

                def dice(x, y):
                    screen.blit(Dice, (x, y))
                dice(DiceX, DiceY)
                game.display.update()
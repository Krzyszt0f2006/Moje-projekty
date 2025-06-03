import pygame
from gra import guziki
import time
pygame.init()
#SETTTING
width=694*2.2
height=694*1.2

#SCREEN
screen=pygame.display.set_mode((width,height))
screen.fill("black")
pygame.display.set_caption("Koniec gry")
exit1=pygame.image.load("assety/EXIT.png").convert_alpha()
wyjscie= guziki.Button(width // 2 - 225, 150, exit1, 0.2)
run=True
while run:
    if wyjscie.draw((screen)):
        with open("menu.py") as plik:
            time.sleep(0.1)
            exec(plik.read())
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
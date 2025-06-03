import pygame
from gra import guziki
import time
pygame.init()
#SETTTING
width=694*2.2
height=694*1.2
#SCREEN
screen=pygame.display.set_mode((width,height))
screen.fill("cadetblue")
pygame.display.set_caption("Poziomy")
run=True
level1=pygame.image.load("assety/ikonka1.png").convert_alpha()
level2=pygame.image.load("assety/ikonka2.png").convert_alpha()
level3=pygame.image.load("assety/ikonka3.png").convert_alpha()
exit1=pygame.image.load('assety/EXIT.png').convert_alpha()




#################################
poziom1= guziki.Button(width // 2 - 710, 100, level1, 0.3)
poziom2= guziki.Button(width // 2 - 710 + 400, 100, level2, 0.3)
poziom3= guziki.Button(width // 2 - 710 + 800, 100, level3, 0.3)
wyjscie= guziki.Button(width // 2 - 710 + 400, 500, exit1, 0.3)
while run:
    screen.fill((52,78,91))
    if poziom1.draw(screen):
        with open("lv1.py") as plik:
            exec(plik.read())
    if poziom2.draw(screen):
        with open("lv2.py") as plik:
            exec(plik.read())
    poziom2.draw(screen)
    poziom3.draw(screen)
    if wyjscie.draw((screen)):
        with open("menu.py") as plik:
            time.sleep(0.1)
            exec(plik.read())

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
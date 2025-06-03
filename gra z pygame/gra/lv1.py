import pygame
from sys import exit
from gra import postac
import platforma
import wrogowie
import portal

#from postac import gracz
pygame.init()
#SETTTING
width=694*2.2
height=694*1.2
#SCREEN
screen=pygame.display.set_mode((width,height))
screen.fill("cadetblue")
pygame.display.set_caption("fajna gra")
#OBJECTS
clock=pygame.time.Clock()
tlo=pygame.image.load('assety/gra_tlo.png')
tlo_width, tlo_height=tlo.get_size()
tlo=pygame.transform.scale(tlo,(tlo_width*2.2,tlo_height*1.2))
run=True
gracz= postac.Player(width // 2, height - 150, 18)
podloga=platforma.Platforma(pygame.image.load("assety/podloga.png").convert_alpha(), 10, 5, 0, 750)
#podloga=platforma.Platforma(pygame.image.load("platforma1_1.png"),10,5,0,418)
wrog=wrogowie.Enemy(900, 710, 6, (pygame.image.load("assety/robot1-A-moving.png").convert_alpha()), 3, 700, 1530)
#portal=pygame.image.load("portal.png").convert_alpha()
portal=portal.Portal(1400, 700, (pygame.image.load("assety/portal.png").convert_alpha()), 2)
while run:
    screen.blit(tlo,(0,0))
    podloga.draw(screen)
    gracz.draw(screen)
    gracz.move()
    gracz.check_collision(podloga)
    gracz.check_collision(portal)
    WHITE = (0, 0, 0)
    portal.draw(screen)
    wrog.draw(screen)
    wrog.move()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
pygame.quit
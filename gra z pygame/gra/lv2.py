import pygame
from sys import exit
pygame.init()
#SETTTING
width=694*2.2
height=694*1.2
#POZYCJE
robot_x=300

robot_y=694*1.2-150
robot_speed=True
#SCREEN
screen=pygame.display.set_mode((width,height))
screen.fill("cadetblue")
pygame.display.set_caption("fajna gra")
#OBJECTS
clock=pygame.time.Clock()
test_surface=pygame.Surface((800,120)).convert()
tlo=pygame.image.load('assety/gra_tlo.png')
tlo_width, tlo_height=tlo.get_size()
tlo=pygame.transform.scale(tlo,(tlo_width*2.2,tlo_height*1.2))
platforma=pygame.Surface((694*2.2,200)).convert()
platforma.fill("black")
#ROBOT ENEMY
robot=pygame.image.load("assety/robot1_A.png").convert_alpha()
robot_width, robot_height = robot.get_size()
robot=pygame.transform.scale(robot, (robot_width * 3,   robot_height * 3))
robot_rect=robot.get_rect(midbottom=(robot_x,760))

#WORLD
test_surface.fill("green")

#GRACZ
gracz_surface=pygame.image.load("assety/placeholder.png").convert_alpha()  #convert_alpha poprawia optymalizacje
#gracz_surface = pygame.transform.flip(gracz_surface, True, False)
gracz_surface_width, gracz_surface_height=robot.get_size()
gracz_surface=pygame.transform.scale(gracz_surface,(gracz_surface_width*1.1,gracz_surface_height*1.1))
gracz_rect=gracz_surface.get_rect(midbottom=(80,750))
gracz_grawitacja=0
#print(gracz_rect.y)
#RUN GAME
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gracz_rect.bottom >= 750:
                print("jump")
                gracz_grawitacja -= 25

        keys = pygame.key.get_pressed()  # Sprawdza aktualny stan klawiszy
    if keys[pygame.K_d]:
        gracz_rect.right += 18
    if keys[pygame.K_a]:
        gracz_rect.left -= 18
    screen.blit(tlo,(0,0))
    screen.blit(platforma,(0,750))
    #screen.blit(test_surface,(0,280))
    screen.blit(robot,robot_rect)
    if robot_speed:
        #robot_x+=5
        robot_rect.right+=6
    else:
        robot_rect.left-=6
    if robot_rect.right>=694*2.2-50:
    #if robot_x>=694*2.2-50:
        robot_speed=False
        robot=pygame.transform.flip(robot,True,False)
    if robot_rect.left<=0:
    #if robot_x<=250:
        robot_speed=True
        robot = pygame.transform.flip(robot, True, False)
    screen.blit(gracz_surface,(gracz_rect))
    #print(gracz_rect.colliderect(robot_rect))
    if gracz_rect.colliderect(robot_rect):
        print("collision")
        #pygame.quit()
        with open("game_over.py") as plik:
            exec(plik.read())
    #gracz
    gracz_grawitacja+=0.7
    gracz_rect.y+=gracz_grawitacja

    print(gracz_rect.bottom)
    if gracz_rect.bottom>=750:
        gracz_rect.bottom=750
        gracz_grawitacja=0
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print("jump")
    #print(gracz_rect.y)
    pygame.display.update()
    clock.tick(60)
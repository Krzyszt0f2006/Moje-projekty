import pygame
import guziki
import time

pygame.init()
#SETTTING
width=694*2.2
height=694*1.2
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Menu")
#Czcionka
czcionki=pygame.font.SysFont("arialblack", 60)
#KOLOR
kolory=(255,255,255)
#guziki
start_img=pygame.image.load("assety/START.png").convert_alpha()
ustawienia_img=pygame.image.load("assety/USTAWIENIA.png").convert_alpha()
rekordy_img=pygame.image.load("assety/REKORDY.png").convert_alpha()
poziomy_img=pygame.image.load("assety/POZIOMY.png").convert_alpha()
exit_img=pygame.image.load("assety/EXIT.png").convert_alpha()
#start_width, start_height=start_img.get_size()
#start_img=pygame.transform.scale(start_img,(start_width//5,start_height//5))
#button instances
start_button= guziki.Button(width // 2 - 180, 100, start_img, 0.15)
ustawienia_button= guziki.Button(width // 2 - 180, 240, ustawienia_img, 0.15)
rekordy_button= guziki.Button(width // 2 - 180, 240 + 140, rekordy_img, 0.15)
poziomy_button= guziki.Button(width // 2 - 180, 240 + 280, poziomy_img, 0.15)
exit_button= guziki.Button(width // 2 - 180, 240 + 420, exit_img, 0.15)
def rysuj(tekst,czcionka,kolor,pozycja_x,pozycja_y):
    img=czcionka.render(tekst,True,kolor)
    screen.blit(img, (pozycja_x,pozycja_y))
run = True
while run:
    screen.fill((52,78,91))
    keys = pygame.key.get_pressed()  # Sprawdza aktualny stan klawiszy
    if start_button.draw(screen):
        print("start")
        with open('lv1.py') as plik:
            exec(plik.read())
            run=False
    ustawienia_button.draw(screen)
    rekordy_button.draw(screen)
    if poziomy_button.draw(screen):
        with open("poziomy.py") as plik:
            time.sleep(0.2)
            exec(plik.read())

    if exit_button.draw(screen):
        run=False
    #rysuj("START",czcionki,kolory,width//2-120,150)
    #rysuj("USTAWIENIA",czcionki,kolory,width//2-220,280)
    #rysuj("REKORDY", czcionki, kolory, width // 2 - 180, 280+130)
    #rysuj("POZI    OMY", czcionki, kolory, width // 2 - 170, 280 + 260)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
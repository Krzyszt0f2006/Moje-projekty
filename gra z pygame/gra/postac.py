#gracz klassa
import json

import time
from platforma import Platforma
from portal import Portal
WHITE=(0,0,0)
import pygame
screen_widht=11
screen_height=11
screen=pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption("postac")
postac=pygame.image.load("assety/placeholder.png").convert_alpha()
gracz_surface_width, gracz_surface_height = postac.get_size()
postac = pygame.transform.scale(postac, (gracz_surface_width * 1.2, gracz_surface_height * 1.2))
class Player():
    def __init__(self,x,y,speed):
        self.image=postac
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.witdh, self.height = postac.get_size()
        self.rect=pygame.Rect(0,0, self.witdh,self.height)
        self.rect.center=x,y
        self.flip=False
        self.czy_skok=False
        self.momentum=0
        self.gracz_grawitacja=0
        self.czas_gry=time.time()
    def draw(self,surface):
        screen.blit(pygame.transform.flip(self.image,self.flip, False),self.rect)
        surface.blit(self.image,(self.rect.x,self.rect.y))
        pygame.draw.rect(screen,WHITE,self.rect,2)

    def check_collision(self, other_sprite):
        # Sprawdzanie kolizji z innym sprite'em
        if self.rect.colliderect(other_sprite.rect):
            # Sprawdzanie klasy obiektu, z którym jest kolizja
            if isinstance(other_sprite, Platforma):
                #print("Kolizja z platformą!")
                #print(other_sprite)
                self.czy_skok=True
                self.gracz_grawitacja=0
            else:


                if isinstance(other_sprite, Portal):
                    print("Kolizja z innym obiektem!")
                    end_time = time.time()
                    dzialanie = end_time - self.czas_gry
                    with open("rekordy.json", 'w') as dane:
                        wynik={
                            "Nazwa gracza" : "-",
                            "Czas gry" : dzialanie,
                            "Pokonani wrogowie" : "0"
                        }
                        json.dump(wynik,dane)
                    with open("lv2.py") as plik:
                        exec(plik.read())
    def move(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.czy_skok:
            self.gracz_grawitacja -= 10
            self.momentum=20
            self.czy_skok=False
        if key[pygame.K_a]:
            self.rect.x -=self.speed
            self.flip=True
        if key[pygame.K_d]:
            self.rect.x+=self.speed
            self.flip=False
            pass
        if self.momentum>0:
            self.gracz_grawitacja-=0.1
            self.momentum-=1
        if self.czy_skok==False and self.momentum==0:
            self.gracz_grawitacja += 0.7
        if self.gracz_grawitacja>9:
            self.gracz_grawitacja=9
        self.rect.y += self.gracz_grawitacja
        #print(self.rect.x)
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>1530:
            self.rect.right=1530


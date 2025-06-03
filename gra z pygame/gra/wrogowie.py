import pygame
screen_widht=11
screen_height=11
WHITE=(0,0,0)

screen=pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption("postac")
wrog=pygame.image.load("assety/placeholder.png").convert_alpha()
wrog_surface, gracz_surface_height = wrog.get_size()
wrog = pygame.transform.scale(wrog, (wrog_surface * 1.2, gracz_surface_height * 1.2))
class Enemy():
    def __init__(self,x,y,speed,obraz,skala,granica1,granica2):
        self.granica1=granica1
        self.granica2=granica2
        self.speed=speed
        self.obraz=obraz
        wrog_surface_width, wrog_surface_height = obraz.get_size()
        self.skala = skala
        self.obraz = pygame.transform.scale(self.obraz,
                                            (wrog_surface_width * self.skala, wrog_surface_height * self.skala))
        self.img = self.obraz

        self.rect=self.img.get_rect()
        self.rect.center = (x, y)
        self.witdh, self.height = self.obraz.get_size()
        self.rect = pygame.Rect(0, 0, self.witdh, self.height)
        self.rect.center = x, y
        self.flip = False
        self.strona=False

        #False=lewo  True=prawo
    def draw(self,surface):
        img = self.obraz

       # screen.blit(pygame.transform.flip(img, self.flip, False), self.rect)
        surface.blit(img, (self.rect.x, self.rect.y))
        #pygame.draw.rect(screen,WHITE,self.rect,2)
    def move(self):
        if self.strona:
            if self.rect.x+self.speed>=self.granica2:
                self.strona=False
            else:
                self.rect.x += self.speed
        else:
            if self.rect.x-self.speed<=self.granica1:
                self.strona=True
            else:
                self.rect.x -= self.speed
                self.flip = True

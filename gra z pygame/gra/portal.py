WHITE=(0,0,0)
import pygame
screen_widht=11
screen_height=11
screen=pygame.display.set_mode((screen_widht, screen_height))
class Portal():
    def __init__(self,x,y,obraz,skala):
        self.obraz=obraz
        self.skala=skala
        wrog_surface_width, wrog_surface_height = obraz.get_size()
        self.obraz = pygame.transform.scale(self.obraz,
                                            (wrog_surface_width * self.skala, wrog_surface_height * self.skala))
        self.img = self.obraz

        self.rect = self.img.get_rect()
        self.rect.center = (x, y)
        self.witdh, self.height = self.obraz.get_size()
        self.rect = pygame.Rect(0, 0, self.witdh, self.height)
        self.rect.center = x, y

    def draw(self, surface):
        img = self.obraz
        surface.blit(img, (self.rect.x, self.rect.y))
        #pygame.draw.rect(screen, WHITE, self.rect, 2)

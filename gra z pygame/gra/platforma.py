import pygame
class Platforma():
    def __init__(self, obraz, skala_x, skala_y,x,y):
        width = obraz.get_width()
        height = obraz.get_height()
        self.obraz = pygame.transform.scale(obraz, (int(width * skala_x), int(height * skala_y)))
        self.rect = self.obraz.get_rect()
        self.rect.topleft = (x, y)
    def draw(self,surface):
        surface.blit(self.obraz, (self.rect.x, self.rect.y))
        WHITE = (0, 0, 0)
        #pygame.draw.rect(screen, WHITE, self.rect, 2)
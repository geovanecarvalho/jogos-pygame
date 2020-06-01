import pygame

class Cenario(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.bg = pygame.image.load("img/bg/%s"% image)
        self.image = self.bg
        self.rect = self.image.get_rect()
        self.speed = 0
    
    def velocidade(self, valor):
        self.speed = valor

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right <= 1600:
            self.rect.right = 2400
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, sprites):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprites = sprites
        self.current_sprites = 0
        self.image = self.sprites[self.current_sprites].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]
    def mudarImage(self, image):
        self.sprites = image

    def update(self):
        self.current_sprites += 0.3
        if self.current_sprites >= len(self.sprites):
            self.current_sprites = 0
        self.image = self.sprites[int(self.current_sprites)]
        

def carrengarImage(nome, valor):
    image = []
    for i in range(1, valor + 1):
        image.append(pygame.image.load("img/player/%s (%d).png"%(nome, i)))
    return image
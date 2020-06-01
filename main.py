import pygame, sys
from mapa import Cenario
from jogadores import Player, carrengarImage
#inicializando pygame
pygame.init()

#Configuração de tamanho de tela
width = 800
height = 600
fps = 60

#Renderizando tela
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((width, height))
clock  = pygame.time.Clock()

#Cores
black = (0,0,0)

#Definindo plano de fundo

fundo = Cenario("BG.png")
fundo_group = pygame.sprite.Group()
fundo_group.add(fundo)
fundo_speed = 0
#Definindo jogador

idle = carrengarImage("Idle", 10)
walk = carrengarImage("Walk", 10)

jogador = Player(100, 280, idle)
jogador_group = pygame.sprite.Group()
jogador_group.add(jogador)

while True:
    #delta time
    clock.tick(fps)

    #capturar os eventos da tela
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            #Fecha janela
            pygame.quit()
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                fundo_speed += -5
                fundo.velocidade(fundo_speed)
                jogador.mudarImage(walk)
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                fundo_speed = 0
                fundo.velocidade(fundo_speed)
                jogador.mudarImage(idle)

 

    #colocar cor de fundo
    screen.fill(black)

    #imagem de plano de fundo
    fundo_group.draw(screen)

    #desenhar jogador
    jogador_group.draw(screen)

       

    #Atualizar
    jogador.update()
    fundo.update()
    pygame.display.flip()
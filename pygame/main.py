import pygame

BluVio = (153,102,204)
Red = (255, 36, 0)

pygame.init()
tela = pygame.display.set_mode((770,640))
pygame.display.set_caption('Meu Jogo')

tela.fill((255,255,255))
pygame.draw.ellipse(tela,Red,[255,70,250,250])
pygame.display.flip()

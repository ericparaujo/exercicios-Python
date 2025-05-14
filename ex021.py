import pygame
pygame.init()
pygame.mixer.music.load('Offspring.mp3')
pygame.mixer.music.play()
pygame.event.wait()
sair = (input(' \n ------------------------ \n digite qualquer coisa para sair da musica'))

print('\n obrigado por ouvir musica de qualidade')
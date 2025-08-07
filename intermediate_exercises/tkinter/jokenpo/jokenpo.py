"""
GAME: Pedra, Papel e Tesoura
Implemente um jogo onde o usuário escolhe pedra, papel ou tesoura, o computador também, e o programa decide quem venceu.

"""
from random import choice

JOKENPO = ('pedra', 'papel', 'tesoura') #variaveis constantes sempre em maiusculas (PEP 8)


print(choice(JOKENPO))
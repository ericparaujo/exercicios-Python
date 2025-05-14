from random import randint
from time import sleep

aleatorio = randint(1,10)
contador = 0
acertou = False

while not acertou:
    escolha = int(input('digite um numero: '))
    contador += 1
    if aleatorio == escolha:
        acertou = True

print(f'eu escolhi {aleatorio} e voce escolheu {escolha}')
print(f'voce tentou {contador} vezes')
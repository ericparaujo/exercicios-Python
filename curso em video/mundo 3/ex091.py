from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ordens = {}

ordem = sorted(jogo.items(), key=itemgetter(1))

for k, v in ordem:
    sleep(1)
    print(f'o {k} tirou {v} no dado')

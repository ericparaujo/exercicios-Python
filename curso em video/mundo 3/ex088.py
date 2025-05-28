from random import randint
from time import sleep

sorteio = []
sorteio_total = []
jogos = int(input('digite a quantidade de jogos: '))
sena = 0

while True:
    for j in range(0, jogos):
        c = 0
        while c in range(0, 6):
            sena = randint(1, 60)
            if sena not in sorteio:
                sorteio.append(sena)
                sorteio.sort()
                c += 1
        sorteio_total.append(sorteio[:])
        sorteio.clear()
    break

print('=====' * 5)

for i, p in enumerate(sorteio_total):
    sleep(1)
    print(f'jogo {i + 1}: {p}')


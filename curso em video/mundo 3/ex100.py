from random import randint


def sorteia(num):
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'os numeros sorteados foram: {num}')


def somaPar(num):
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print(f'a soma dos numeros pares sao: {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)



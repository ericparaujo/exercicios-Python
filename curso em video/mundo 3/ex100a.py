from random import randint


def sorteia(num):
    for c in range(0, 5):
        num.append(randint(1, 10))

    return num


def somar(num):
    soma = 0
    for s in num:
       soma += s

    return soma


numeros = []

print(sorteia(numeros))
print(somar(numeros))

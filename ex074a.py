from random import randint

lista = []
mega = int(input('digite quantos numeros a ser sorteados: '))

for c in range(mega):
    lista.append(randint(1,100))

tupla = tuple(lista)
lista.clear()
del lista

print(sorted(tupla))
print(f' o maior é: {max(tupla)}')
print(f' o menor é: {min(tupla)}')

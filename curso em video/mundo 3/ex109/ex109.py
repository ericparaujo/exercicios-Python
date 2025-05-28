import moeda

valor = float(input('digite um valor: '))
porcento = int(input('porcentagem: '))

metade = (moeda.metade(valor))
dobro = (moeda.dobro(valor))
aumento = moeda.aumentar(valor, porcento)
reducao = moeda.diminuir(valor, porcento)

print(f'metade: {moeda.metade(valor, True)}')
print(f'dobro: {moeda.dobro(valor, True)}')
print(f'aumento: {moeda.aumentar(valor, porcento, True)}')
print(f'reducao: {moeda.diminuir(valor, porcento, True)}')
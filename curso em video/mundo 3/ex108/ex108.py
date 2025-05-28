import moeda

valor = float(input('digite um valor: '))
porcento = int(input('porcentagem: '))

metade = (moeda.metade(valor))
dobro = (moeda.dobro(valor))
aumento = moeda.aumentar(valor, porcento)
reducao = moeda.diminuir(valor, porcento)

print(f'metade: {moeda.moeda(metade)}')
print(f'dobro: {moeda.moeda(dobro)}')
print(f'aumento: {moeda.moeda(aumento)}')
print(f'reducao: {moeda.moeda(reducao)}')

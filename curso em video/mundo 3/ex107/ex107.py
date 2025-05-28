import moeda

num = int(input('digite um numero: '))
taxa = int(input('digite a taxa: '))

print(f'aumento de {taxa}% de {num} = {moeda.aumentar(num, taxa)}')
print(f'reducao de {taxa}% de {num} = {moeda.diminuir(num, taxa)}')
print(f'metade  de {num} = {moeda.metade(num)}')
print(f'dobro   de {num} = {moeda.dobrar(num)}')

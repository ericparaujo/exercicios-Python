lista = []
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input(f'digite o valor da posicao {c}: ')))
    if c == 0:
        maior = menor = lista[0]
    else:
        if maior <= lista[c]:
            maior = lista[c]
        if menor >= lista[c]:
            menor = lista[c]

print(f' lista = {lista}')
print(f'menor = {menor}')
print(f' o maior valor é {maior} e a posicao é ', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end=' ')

print(f'\no menor valor é {menor} e a posicao é', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end=' ')
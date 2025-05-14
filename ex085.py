lista_total = [[], []]          # variavel principal

for c in range(1, 8):           # loop
    valor = int(input(f'digite o {c}° valor: '))

    if valor % 2 == 0:          #condicionais
        lista_total[0].append(valor)
    else:
        lista_total[1].append(valor)

lista_total[0].sort()           #ordenar valores
lista_total[1].sort()

print(f'total: {lista_total}')  #resultado na tela
